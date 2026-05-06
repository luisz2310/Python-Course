# while loop = repeats while condition is True

# basic while
i = 0
while i < 5:
    print(i)
    i += 1

# countdown example
n = 3
while n > 0:
    print(n)
    n -= 1


# break = stop loop completely
x = 0
while True:
    if x == 3:
        break
    print("break:", x)
    x += 1

# Output:
# break: 0
# break: 1
# break: 2


# continue = skip current iteration
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("continue:", i)

# Output:
# continue: 1
# continue: 2
# continue: 4
# continue: 5


# pass = does nothing (placeholder)
i = 0
while i < 5:
    if i == 3:
        pass
    print("pass:", i)
    i += 1

# Output:
# pass: 0
# pass: 1
# pass: 2
# pass: 3
# pass: 4

# pass -> does NOTHING and continues normal flow
# (used as a placeholder when code is needed syntactically but not implemented)


# while with collection
nums = [1, 2, 3]
while nums:
    print(nums.pop())