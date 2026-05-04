import os
import sys

print("Generating cards...")
result = os.system(f"{sys.executable} generate.py")
if result != 0:
    print("Error: Card generation failed.")
    sys.exit(1)

print("Pushing to Anki...")
result = os.system(f"{sys.executable} push_to_anki.py")
if result != 0:
    print("Error: Push to Anki failed.")
    sys.exit(1)

print("Done.")
