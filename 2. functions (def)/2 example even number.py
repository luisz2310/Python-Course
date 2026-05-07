# contains_even = checks if a list contains at least one even number

# version 1 (correct idea but incomplete)
def contains_even(nums):
    for n in nums:
        if n % 2 == 0:
            return True
        else:
            pass

# problem:
# - returns True immediately when it finds an even number
# - but if no even number exists, it returns None (implicit)

# version 2 (wrong logic)
def contains_even(nums):
    for n in nums:
        if n % 2 == 0:
            return True
        else:
            return False

# problem:
# - only checks the FIRST element
# - does NOT check the full list

# version 3 (still wrong logic)
def contains_even(nums):
    for n in nums:
        if n % 2 == 0:
            return True
        else:
            return False
    return None

# problem:
# - still returns after first element
# - return False inside loop breaks logic
# - return None only happens if list is empty

# correct version (final solution)
def contains_even(nums):
    for n in nums:
        if n % 2 == 0:
            return True
    return False

# explanation:
# - loop through all numbers
# - if any number is even -> return True immediately
# - if loop finishes with no even numbers -> return False


# key concepts:
# return -> stops function immediately
# loop -> goes through each element one by one
# correct logic -> only return False AFTER checking everything