# 🧠 Python Classes Cheat Sheet

# ---------------------------
# 1. Basic class definition
# ---------------------------
class SampleClass:
    pass

class SampleClass2():
    pass

sample = SampleClass()
sample2 = SampleClass2()

print(type(sample))   # <class '__main__.SampleClass'>
print(type(sample2))  # <class '__main__.SampleClass2'>

print("--------------")


# ---------------------------
# 2. Constructor (__init__)
# ---------------------------
class ClassInit:
    def __init__(self):
        print("Init Class")

ClassInit()  # automatically calls __init__

print("--------------")


# ---------------------------
# 3. Instance attributes
# ---------------------------
class Dog:
    def __init__(self, name, age, w):
        self.name = name
        self.age = age
        self.weight = w

# dog0 = Dog("Bob") ❌ error: missing arguments

dog1 = Dog("Bob", 25, 10)
print(dog1.name)
print(dog1.age)
print(dog1.weight)

# using named arguments (order doesn't matter)
dog2 = Dog(age=20, name="Mark", w=5)
print(dog2.name)
print(dog2.age)
print(dog2.weight)

print("--------------")


# ---------------------------
# 4. Class vs Instance attributes
# ---------------------------
class Attributes:
    plan = "default"  # class attribute (shared)

    def __init__(self, name, age):
        self.name = name
        self.age = age

att = Attributes(name="Bob", age=20)

print(att.plan)          # access class attribute via instance
print(Attributes.plan)   # access via class

# overriding class attribute at instance level
att.plan = "premium"

print(att.plan)          # "premium" (instance value)
print(Attributes.plan)   # "default" (class unchanged)


# ---------------------------
# 🔑 SUMMARY
# ---------------------------
# - class: blueprint for objects
# - __init__: constructor (runs when creating object)
# - self: reference to the instance
# - instance attributes: unique per object
# - class attributes: shared across all instances