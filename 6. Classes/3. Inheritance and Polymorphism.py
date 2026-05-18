# 🧠 Inheritance & Polymorphism in Python

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_am_i(self):
        print(self.name, self.age)

    def eat(self):
        print('I am eating')


# ---------------------------
# 1. Inheritance + Override
# ---------------------------
class Dog(Animal):
    def __init__(self):
        super().__init__(name='dog', age=0)  # better than Animal.__init__

    def eat(self):  # override
        print('I am a dog eating')


p = Dog()
p.who_am_i()
p.eat()

print('--------------')


# ---------------------------
# 2. Another subclass
# ---------------------------
class Cat(Animal):
    def __init__(self):
        super().__init__(name='cat', age=0)

    def eat(self):  # override
        print('I am a cat eating')

    def sleep(self):
        print('I am a cat sleeping')


c = Cat()

c.who_am_i()
c.eat()

print('--------------')


# ---------------------------
# 3. Polymorphism
# ---------------------------
pets = [c, p]

for pet in pets:
    pet.who_am_i()
    pet.eat()
    # pet.sleep() ❌ not safe (Dog doesn't have sleep)


# ---------------------------
# 🔑 Key Concepts
# ---------------------------
# - Inheritance: Dog/Cat inherit from Animal
# - Method overriding: each class defines its own eat()
# - super(): recommended way to call parent constructor
# - Polymorphism: same method call behaves differently per object
# - Only call methods guaranteed to exist for all objects in the list


# ---------------------------
# 💡 Pro Tip (safe polymorphism)
# ---------------------------
for pet in pets:
    if hasattr(pet, "sleep"):
        pet.sleep()  # ✅ safe check before calling