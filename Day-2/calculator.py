class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        add = num1 + num2
        print("Sum:", add)

        sub = num1 - num2
        print("Sub:", sub)

        mult = num1 * num2
        print("Product:", mult)

        div = num1 / num2
        print("Division:", div)


pair1 = Calculator(8, 4)  # creating instances of the class

pair1.calculate()         # calling method on the instances
