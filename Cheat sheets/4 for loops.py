# for loop = iterate over collections

nums = [1, 2, 3, 4, 5, 6, 7]
text = "hello"
s = {1, 2, 3}
d = {"a": 1, "b": 2}

# basic iteration
for n in nums:
    print(n)

for ch in text:
    print(ch)

for item in s:
    print(item)

# dictionary iteration
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

# enumerate (index + value)
for i, v in enumerate(nums):
    print(i, v)
# basic enumerate
nums = [10, 20, 30]
for i, n in enumerate(nums):
    print(i, n)

# start index from 1
nums = [10, 20, 30]
for i, n in enumerate(nums, start=1):
    print(i, n)

# use with strings
text = "abcdefg"
for i, ch in enumerate(text):
    print(i, ch)

# use only index
nums = [1, 2, 3, 4, 5, 6, 7]
for i, _ in enumerate(nums):
    print(i)

# range
for i in range(3):
    print(i)

# slicing in for loop ([::] / [:])

for n in nums[::2]:
    print("step 2:", n)

for n in nums[::-1]:
    print("reverse:", n)

for ch in text[:3]:
    print("first part:", ch)

for ch in text[-3:]:
    print("last part:", ch)

for ch in text[:-3]:
    print("first part negative:", ch)

for ch in text[-2:-3]:
    print("nothing:", ch)

# zip (combine multiple collections)
names = ["a", "b", "c"]
ages = [10, 20, 30]

for name, age in zip(names, ages):
    print(name, age)

# unpacking (sub-collections)
pairs = [(1, 2), (3, 4), (5, 6)]

for a, b in pairs:
    print(a, b)

# list of lists unpacking
pairs2 = [[10, 20], [30, 40]]

for a, b in pairs2:
    print(a + b)

# nested structure unpacking
data = [(1, (2, 3)), (4, (5, 6))]

for a, (b, c) in data:
    print(a, b, c)

# condition + membership inside loop
allowed = {(1, 2), (5, 6)}

for a, b in pairs:
    if (a, b) in allowed:
        print("allowed:", a, b)
