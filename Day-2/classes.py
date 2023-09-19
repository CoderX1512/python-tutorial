"""
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# creating instances of the class

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Ahesh", 22)

# calling methods on instances
person1.greet()
person2.greet()
person3.greet()

"""

"""
class Employee:
    def __init__(self, fname, lname):  # constructor
        self.fname = fname
        self.lname = lname

    def GetFirstName(self):
        print(f"Hello, my first name is {self.fname}.")

    def GetLastName(self):
        print(f"Hello, my last name is {self.lname}.")


# creating instances of the class

person1 = Employee("Ahesh", "Behera")
person2 = Employee("Siddarth", "Das")

# calling methods on instances
person1.GetFirstName()
person1.GetLastName()
person2.GetFirstName()
person2.GetLastName()
"""

class Employee:
    def __init__(self, name):  # constructor
        self.name = name


    def GetFirstName(self):
        print(f"Hello, my first name is {self.fname}.")

    def GetLastName(self):
        print(f"Hello, my last name is {self.lname}.")


# creating instances of the class

person1 = Employee("Ahesh", "Behera")
person2 = Employee("Siddarth", "Das")

# calling methods on instances
person1.GetFirstName()
person1.GetLastName()
person2.GetFirstName()
person2.GetLastName()
