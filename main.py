import os

COUNT = "47"

# The entry must be one number, digits only, of 1-5 characters.
assert 1 <= len(COUNT) <= 5, f"count is {len(COUNT)} chars"
assert COUNT.isdigit(), "digits only"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(COUNT)
