import json, requests, os
from dotenv import load_dotenv

load_dotenv()
DECK = os.getenv("DECK_NAME")

def add_card(card):
    return requests.post("http://localhost:8765", json={
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": DECK,
                "modelName": "Basic",
                "fields": {
                    "Front": card["front"],
                    "Back": card["back"]
                },
                "tags": card.get("tags", [])
            }
        }
    }).json()

with open("cards.json", encoding="utf-8") as f:
    cards = json.load(f)

for c in cards:
    add_card(c)

print("Pushed to Anki")