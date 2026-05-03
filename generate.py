import os, json, hashlib, sys
from dotenv import load_dotenv
import requests
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL = os.getenv("MODEL_NAME")

ROOT = Path(os.getenv("DATA_ROOT", "./Data Structures & Algorithms"))

MAX_CHARS = 4000
MIN_LINES = 4

def read_prompt():
    prompt_file = Path("prompt.md")
    if not prompt_file.exists():
        raise FileNotFoundError(f"prompt.md not found in current directory: {Path.cwd()}")
    with open(prompt_file, encoding="utf-8") as f:
        return f.read()

def get_problem_folders(root):
    for dirpath, _, filenames in os.walk(root):
        py_files = [f for f in filenames if f.endswith(".py")]
        if py_files:
            yield dirpath, py_files

def read_and_dedupe(folder, files):
    seen = set()
    content = []

    for f in files:
        path = os.path.join(folder, f)

        try:
            with open(path, encoding="utf-8") as file:
                code = file.read().strip()
        except UnicodeDecodeError as e:
            print(f"Warning: Skipping {f} due to encoding error: {e}", file=sys.stderr)
            continue
        except IOError as e:
            print(f"Warning: Skipping {f} due to IO error: {e}", file=sys.stderr)
            continue

        if len(code.splitlines()) < MIN_LINES:
            continue

        h = hashlib.md5(code.encode()).hexdigest()
        if h in seen:
            continue
        seen.add(h)

        content.append(f"# {f}\n{code}")

    return "\n\n".join(content)

def truncate(text):
    return text[:MAX_CHARS] if len(text) > MAX_CHARS else text

def call_openai(system_prompt, user_input):
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    if not BASE_URL:
        raise ValueError("OPENAI_BASE_URL not found in environment variables")
    if not MODEL:
        raise ValueError("MODEL_NAME not found in environment variables")
    
    try:
        res = requests.post(
            f"{BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.3
            },
            timeout=30
        )
        res.raise_for_status()
        data = res.json()

        if "choices" not in data:
            raise ValueError(f"Unexpected API response format: {data}")

        return data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse API response: {e}")

def main():
    prompt = read_prompt()
    all_cards = []

    for folder, files in get_problem_folders(ROOT):
        problem = os.path.basename(folder)

        code = read_and_dedupe(folder, files)
        if not code.strip():
            continue

        code = truncate(code)

        user_input = f"Problem: {problem}\n\nCode:\n{code}"

        print("Processing:", problem)

        try:
            output = call_openai(prompt, user_input)
            cards = json.loads(output)

            for c in cards:
                c.setdefault("tags", [])
                c["tags"].append(f"problem/{problem}")

            all_cards.extend(cards)

        except Exception as e:
            print(f"Error processing {problem}: {e}", file=sys.stderr)
            continue

    try:
        with open("cards.json", "w", encoding="utf-8") as f:
            json.dump(all_cards, f, indent=2, ensure_ascii=False)
        print(f"\nDone. Total cards: {len(all_cards)}")
    except IOError as e:
        print(f"Error saving cards.json: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()