try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print("Result: ", result)

except ZeroDivisionError:
    print("Error: cannot divide by zero ")
except ValueError:
    print("Error: invalid input,please enter valid character")
except Exception as e:
    print("Error: An unexpected error occurred ", e)