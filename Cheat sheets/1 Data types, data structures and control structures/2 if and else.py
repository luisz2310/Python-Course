# if / elif / else = runs code based on conditions


# basic if
x = 5
if x > 3:
    print("x is greater than 3")

# Output:
# x is greater than 3


# if - else
x = 2
if x > 3:
    print("x is greater than 3")
else:
    print("x is NOT greater than 3")

# Output:
# x is NOT greater than 3


# if - elif - else
x = 3
if x > 3:
    print("x is greater than 3")
elif x == 3:
    print("x is equal to 3")
else:
    print("x is less than 3")

# Output:
# x is equal to 3


# multiple elif
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Output:
# Grade: B


# nested if
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")

# Output:
# x is between 5 and 15


# pass = placeholder (do nothing)
x = 5
if x > 0:
    pass
else:
    print("negative")

# Output:
# (no output)


# if with collections
nums = [1, 2, 3]
if nums:
    print("list is not empty")

# Output:
# list is not empty


# if / elif / else summary:
# if -> first condition
# elif -> additional conditions (optional, can have many)
# else -> runs if none of the above are True (optional)