Generate Anki cards for DSA problems.

Rules:
- Max 3 cards
- Only DSA concepts (arrays, trees, graphs, DP, etc.)
- Ignore databases, APIs, non-DSA topics
- Each card = 1 idea
- Answers must be <= 2 lines

Output JSON only:
{
  "cards": [
    {
      "front": "",
      "back": "",
      "tags": ["pattern/..."]
    }
  ]
}

Types:
1. Pattern (when to use)
2. Key idea
3. Common mistake

Example:
Input: two sum
Output:
{
  "cards": [
    {
      "front": "When use hashmap in arrays?",
      "back": "When needing O(1) lookup for complements.",
      "tags": ["pattern/hashmap"]
    }
  ]
}

Return ONLY JSON. No text.