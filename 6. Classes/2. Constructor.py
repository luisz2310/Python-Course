# 🧠 Python Class Methods & Attributes (clean example)

class Person:
    salary = 0  # class attribute (shared default)

    def __init__(self, name, age, salary=0):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary  # overrides class attribute for this instance

    # instance method (needs self)
    def display(self):
        print(self.name)
        print(self.age)

    def print_salary(self):
        print(f"Salary: {self.salary}")

    def set_salary(self, salary):
        self.salary = salary


# ---------------------------
# Usage
# ---------------------------
p1 = Person("Bob", 20, 10)

p1.display()
p1.print_salary()

p1.set_salary(15)

p1.display()
p1.print_salary()


# ---------------------------
# 🔑 Notes
# ---------------------------
# - No constructor overloading in Python → use default values instead
# - "self" is required in instance methods to access object data
# - Methods = functions inside a class
# - Class attributes are shared, but instance attributes override them
# - Always use self.attribute to access instance data


# ---------------------------
# ➕ Optional: Static method example
# ---------------------------
class Example:
    @staticmethod
    def test():
        print("test")

Example.test()  # ✅ works without creating an object