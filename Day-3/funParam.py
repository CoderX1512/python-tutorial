# Defining a function with parameters and return value

def calculate_power(base, exponent):
    result = base ** exponent
    return result

# calling the function and using the return value


base_value = 2
exponent_value = 3

power_result = calculate_power(base_value, exponent_value)
print(f"{base_value} raised to the value of {exponent_value} is {power_result}")
