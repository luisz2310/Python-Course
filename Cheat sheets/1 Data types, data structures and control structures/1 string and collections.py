# String assignment and formatting
test: str = 'hello world 2'
print(test)

# f-string
s = f'test {test}'
print(s)

# format method
s = 'test {}'.format(test)
print(s)

# substring and slicing in Python

text = "hello world"

# basic slicing: [start:end]
print(text[0:5])   # hello
print(text[6:11])  # world

# start from beginning
print(text[:5])    # hello

# go to end
print(text[6:])    # world

# negative indexing
print(text[-5:])   # world
print(text[:-6])   # hello

# step slicing: [start:end:step]
print(text[::2])   # hlowrd (every 2nd char)
print(text[::-1])  # reverse string

# substring check (membership)
if "hello" in text:
    print("found hello")

# loop over substring
for ch in text[:5]:
    print(ch)

# extracting words manually
word1 = text[:5]
word2 = text[6:]
print(word1, word2)

# List
l = [0,1,2,3,4,5,6]
print(l)
l.pop()
print(l)
l.pop(1)
print(l)
l.pop(3)
print(l)

# Dictionary and variable reference behavior
r = 'r'
d = {'a': 'a', 'b': 'b', 'r': r}

print(d['a'].upper())  # A
print(d)

print(d['r'].upper())  # R (value from dict)

# Change original variable (does NOT affect dict)
r = 'R'
print(d['r'].upper())  # still 'R' from original 'r'
print(d)

# Tuple (immutable)
tuple1 = (1, 2, 3)
print(tuple1[2])

# Set (mutable)
set1 = {1, 2, 3}
#print(set1[1])

# Store set inside dictionary
d = {'s': set1}
print(d)

# Modify set (affects dictionary because it's the same reference)
set1.add(4)
print(d)

# Reassign set1 (does NOT affect dictionary)
set1 = {1, 2}
print(d)

# String comparison (lexicographical)
print('test' > 'abcfd')  # True

# Collection types summary:
# list  -> ordered, mutable, allows duplicates [1,2,3,4]
# tuple -> ordered, immutable, allows duplicates (1,2,3,3,4)
# set   -> unordered, unique items only {2,3,1}
# dict  -> key-value pairs, keys must be unique {'1':1,'2':2,'3':3}
