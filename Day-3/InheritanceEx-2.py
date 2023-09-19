# Base class (Parent class)
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass
# Derived class (Child class) inheriting from the shape (Parent class)


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Derived class (Child class) inheriting from the shape (Parent class)
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating instances of the derived class


circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# calling the speak methods on these objects
print(f"Area of the {circle.color} circle: {circle.area():.2f} square units ")
print(f"Area of the {rectangle.color} rectangle: {rectangle.area():.2f} square units")
