# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of the derived class


dog = Dog("Buddy")
cat = Cat("Whiskers")

# calling the speak methods on these objects
print(f"{dog.name} says: {dog.speak()} ")
print(f"{cat.name} says: {cat.speak()} ")
