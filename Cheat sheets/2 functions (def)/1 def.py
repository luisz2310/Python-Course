# def = used to define a function (a reusable block of code)

# parts of a function:
# def -> keyword to define a function
# function_name -> name of the function all in low case and _ to separate words
# parameters -> inputs inside parentheses (optional)
# default parameters -> values used if no argument is provided
# body -> code inside the function
# return -> sends a value back (optional)



# basic function structure
def function_name():
    # function body
    print("Hello")


# function with parameter
def greet(name):
    print("Hello", name)

# function with return value
def add(a, b):
    return a + b

# function with default parameter
def greet2(name="friend"):
    print("Hello", name)

# example usage
greet("Luis")
greet2()
greet2("Sam")
result = add(2, 3)
print(result)

#call without () return the function
print(function_name)

def sum_return(num1, num2):
    return num1 + num2
