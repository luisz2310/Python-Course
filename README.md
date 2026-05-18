# Python Course 🚀

This repository is a collection of Python cheat sheets and practical examples designed to learn Python from basics to intermediate concepts in a simple and structured way.

---

## 📁 Structure

    Cheat sheets/
    ├───1. Data types, data structures and control structures
    ├───2. functions (def)
    ├───3. Exercises part 1
    ├───4. lambda, map and filter
    ├───5. Nested statement and scope
    ├───6. Classes
    └───7. Package and Modules

---

## 📚 Topics Covered

### 1. Data Types, Control Flow & Structures
- Strings, Lists, Tuples, Sets, Dictionaries
- if / elif / else
- for / while loops
- break / continue / pass
- list comprehensions

Example:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

---

### 2. Functions (def)
- Function definition
- Parameters and return values
- Default arguments

Example:
    def greet(name="friend"):
        print("Hello", name)

    def add(a, b):
        return a + b

---

### 3. Exercises (Part 1)

Contains Even:
    def contains_even(nums):
        for n in nums:
            if n % 2 == 0:
                return True
        return False

String Transformation:
    vowels = ('a','e','i','o','u')

    def myfunc(input_string):
        return "".join(
            c.lower() if c.lower() in vowels else c.upper()
            for c in input_string
        )

---

### 4. Lambda, Map & Filter

Example:
    r = list(map(lambda x: x * 2, [1, 2, 3, 4]))
    l = list(filter(lambda x: x % 2, range(10)))

---

### 5. Nested Statements & Scope (LEGB)

Example:
    z = 10

    def f():
        z = 15
        print(z)

    f()
    print(z)

- L = Local  
- E = Enclosing  
- G = Global  
- B = Built-in  

---

### 6. Classes (OOP)

Classes:
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

Methods:
    class Person:
        def __init__(self, name, age, salary=0):
            self.name = name
            self.age = age
            self.salary = salary

        def display(self):
            print(self.name, self.age)

Inheritance:
    class Animal:
        def eat(self):
            print("eating")

    class Dog(Animal):
        def eat(self):
            print("dog eating")

Dunder Methods:
    class Book:
        def __init__(self, title, pages):
            self.title = title
            self.pages = pages

        def __str__(self):
            return self.title

        def __len__(self):
            return self.pages

---

### 7. Packages & Modules

Concepts:
- Importing modules
- Creating your own modules
- Using packages

Example:
    import math
    print(math.sqrt(16))

    # custom module
    # mymodule.py
    def greet():
        print("Hello from module")

    # main file
    import mymodule
    mymodule.greet()

---

## 🛠 Tech Stack
- Python 3.x  
- VS Code / PyCharm  
- Git & GitHub  

---

## 🚀 Author
Luisz Bautista