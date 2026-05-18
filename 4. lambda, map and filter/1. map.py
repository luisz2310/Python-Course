# map = applies a function to each item in an iterable


# function
def multiply(num):
    return num * 2


# use map
r = list(map(multiply, [1, 2, 3, 4]))
print(r)


# map with lambda (no named function)
r = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(r)


# map with strings (reverse each string)
r = ['Test', 'Local', 'Random']
l1 = list(map(lambda x: x[::-1], r))
print(l1)


# map summary:
# map(function, iterable) -> applies function to each element
# returns an iterator (convert to list if needed)