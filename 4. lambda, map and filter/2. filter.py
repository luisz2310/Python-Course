# filter = selects elements from an iterable based on a condition


# lambda function (returns remainder)
f = lambda n: n % 2


# use filter
l = list(filter(f, range(10)))
print(l)


# cleaner version (direct condition)
l = list(filter(lambda x: x % 2 != 0, range(10)))
print(l)

# filter summary:
# filter(function, iterable) -> keeps elements where function returns True
# returns an iterator (convert to list if needed)