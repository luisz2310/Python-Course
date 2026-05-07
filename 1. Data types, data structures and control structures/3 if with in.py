# "if x in ..." checks membership (whether x exists in a collection)

# List / Tuple (checks values)
nums = [1, 2, 3]
if 2 in nums:
    print("2 is in the list")

# String (checks substring)
text = "hello"
if "he" in text:
    print("substring found")

# Set (fast membership check)
s = {1, 2, 3}
if 3 in s:
    print("3 is in the set")

# Dictionary (checks KEYS, not values)
d = {"a": 1, "b": 2}

if "a" in d:
    print("key 'a' exists")

# To check values in a dict:
if 1 in d.values():
    print("value 1 exists")

# To check key-value pairs:
if ("a", 1) in d.items():
    print("pair exists")