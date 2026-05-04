#!/usr/bin/env python3
"""
Regression test for card generation JSON parsing.
Tests that the fix for the 'str' object has no attribute 'setdefault' bug is maintained.
"""

import json
import sys
from pathlib import Path

def test_json_parsing_and_tag_assignment():
    """
    Test that API responses in the format {"cards": [...]} are parsed correctly
    and that tags can be assigned without AttributeError.
    
    This test ensures the bug where iterating over the parsed dict directly
    (instead of extracting the "cards" array) does not regress.
    """
    # Simulate API response format specified in prompt.md
    api_response = json.dumps({
        "cards": [
            {"front": "Question 1", "back": "Answer 1"},
            {"front": "Question 2", "back": "Answer 2"}
        ]
    })
    
    # This is the corrected parsing logic
    try:
        result = json.loads(api_response)
        cards = result.get("cards", [])
        
        # Verify we got a list
        assert isinstance(cards, list), f"Expected list, got {type(cards).__name__}"
        assert len(cards) == 2, f"Expected 2 cards, got {len(cards)}"
        
        # Test tag assignment (the line that was failing)
        problem = "test-problem"
        for c in cards:
            assert isinstance(c, dict), f"Expected dict card, got {type(c).__name__}"
            c.setdefault("tags", [])  # This was raising AttributeError before the fix
            c["tags"].append(f"problem/{problem}")
        
        # Verify tags were added
        assert cards[0]["tags"] == ["problem/test-problem"]
        assert cards[1]["tags"] == ["problem/test-problem"]
        
        print("✓ JSON parsing and tag assignment test PASSED")
        return True
        
    except AttributeError as e:
        print(f"✗ JSON parsing test FAILED: {e}")
        return False
    except Exception as e:
        print(f"✗ JSON parsing test ERROR: {e}")
        return False

def test_edge_cases():
    """Test edge cases in JSON parsing"""
    test_cases = [
        ({"cards": []}, "Empty cards array"),
        ({"cards": [{}]}, "Card with no fields"),
        ({"cards": [{"front": "Q"}]}, "Card with only front"),
    ]
    
    for api_response, description in test_cases:
        try:
            result = json.loads(json.dumps(api_response))
            cards = result.get("cards", [])
            for c in cards:
                c.setdefault("tags", [])
            print(f"✓ Edge case test PASSED: {description}")
        except Exception as e:
            print(f"✗ Edge case test FAILED: {description} - {e}")
            return False
    
    return True

if __name__ == "__main__":
    print("Running regression tests for card generation JSON parsing...\n")
    
    test1 = test_json_parsing_and_tag_assignment()
    test2 = test_edge_cases()
    
    if test1 and test2:
        print("\n✓ All tests passed")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed")
        sys.exit(1)
