# 🧠 Special Methods (Magic/Dunder Methods)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # string representation (for print / str)
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    # length behavior (for len)
    def __len__(self):
        return self.pages


# ---------------------------
# Usage
# ---------------------------
b = Book('Metro 2033', 'Dmitry Glukhovsky', 460)

print(str(b))          # calls __str__
print(f'pages {len(b)}')  # calls __len__


# ---------------------------
# 🔑 Key Concepts
# ---------------------------
# - __str__ → defines how the object is shown as a string
# - __len__ → defines behavior for len(object)
# - These are "dunder methods" (double underscore)
# - They let your objects behave like built-in types


# ---------------------------
# ➕ Bonus examples
# ---------------------------
class Example:
    def __str__(self):
        return "Example object"

    def __len__(self):
        return 42

e = Example()

print(e)        # "Example object"
print(len(e))   # 42