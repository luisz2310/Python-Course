# *args / **kwargs = allows functions to accept variable number of arguments


# *args = multiple positional arguments (tuple)
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

add(1, 2, 3)


# *args as tuple
def show_args(*args):
    print(args)

show_args(1, 2, 3)


# **kwargs = multiple keyword arguments (dictionary)
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(name="Luis", age=25)


# access values in **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Luis", age=25)


# mix normal params + *args + **kwargs
def example(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

example(1, 2, 3, 4, x=10, y=20)


# argument order (important)
# 1. normal parameters
# 2. *args
# 3. **kwargs


# summary:
# *args -> collects extra positional arguments into a tuple
# **kwargs -> collects extra keyword arguments into a dictionary