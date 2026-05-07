# List comprehension is used to build lists in a compact way

# 1. Numbers: square values
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
print(squares)  # [1, 4, 9, 16]

# 2. Filtering values
evens = [n for n in nums if n % 2 == 0]
print(evens)  # [2, 4]

# 3. Working with ranges (no original list needed)
range_list = [n for n in range(5)]
print(range_list)  # [0, 1, 2, 3, 4]

# 4. Convert types
str_nums = ["1", "2", "3"]
ints = [int(x) for x in str_nums]
print(ints)  # [1, 2, 3]

# 5. Nested lists flattening
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4, 5, 6]

# 6. Conditional transformation
nums2 = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in nums2]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# 7. Extract values from dictionary
d = {"a": 1, "b": 2, "c": 3}
values = [v for v in d.values()]
print(values)  # [1, 2, 3]

# LIST COMPREHENSION (short guide)

nums2 = [1, 2, 3, 4, 5, 6]

# filter (keep evens)
evens = [x for x in nums2 if x % 2 == 0]

# transform (label all)
labels = ["even" if x % 2 == 0 else "odd" for x in nums2]

# rules:
# [value for x in iterable if condition]   -> filter
# [A if cond else B for x in iterable]     -> transform

# multiply each element of a with each element of b (flattened)

a = [1, 2, 3]
b = [10, 20]

result = [x * y for x in a for y in b]
print(result)
# [10, 20, 20, 40, 30, 60]

# rule:
# for x in a for y in b -> all combinations, flattened list

print(list(range(0,10)))

stri = 'this is a test list of words'
