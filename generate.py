import os, json, hashlib, sys, time
from dotenv import load_dotenv
import requests
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL = os.getenv("MODEL_NAME")

ROOT = Path(os.getenv("DATA_ROOT", "./Data Structures & Algorithms"))

MAX_CHARS = 3000
MIN_LINES = 4

def read_prompt():
    return Path("prompt.md").read_text(encoding="utf-8")

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
            code = Path(path).read_text(encoding="utf-8").strip()
        except:
            continue

        if len(code.splitlines()) < MIN_LINES:
            continue

        h = hashlib.md5(code.encode()).hexdigest()
        if h in seen:
            continue
        seen.add(h)

        content.append(code[:1200])  # smaller per-file limit

    return "\n\n".join(content)

def call_groq(system_prompt, user_input, retries=3):
    for i in range(retries):
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
                    "temperature": 0.1,
                    "max_completion_tokens": 300,
                    "top_p": 1,
                    "response_format": {"type": "json_object"}
                },
                timeout=30
            )

            data = res.json()

            if "choices" in data:
                return data["choices"][0]["message"]["content"]

            print("Retry:", data, file=sys.stderr)

        except Exception as e:
            print(f"Retry error: {e}", file=sys.stderr)

        time.sleep(2 * (i + 1))

    raise RuntimeError("API failed after retries")

def main():
    if not API_KEY:
        raise ValueError("API KEY missing")

    prompt = read_prompt()
    all_cards = []

    for folder, files in get_problem_folders(ROOT):
        problem = os.path.basename(folder)

        code = read_and_dedupe(folder, files)
        if not code.strip():
            continue

        code = code[:MAX_CHARS]

        user_input = f"{problem}\n{code}"

        print("Processing:", problem)

        try:
            output = call_groq(prompt, user_input)
            result = json.loads(output)
            cards = result.get("cards", [])

            for c in cards:
                c.setdefault("tags", [])
                c["tags"].append(f"problem/{problem}")

            all_cards.extend(cards)

        except Exception as e:
            print(f"Error: {problem} -> {e}", file=sys.stderr)

        time.sleep(1.5)

    Path("cards.json").write_text(
        json.dumps(all_cards, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\nDone. Total cards: {len(all_cards)}")

if __name__ == "__main__":
    main()