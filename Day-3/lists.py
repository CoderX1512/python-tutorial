# Creating a list of numbers
numbers = [19, 37, 44, 63, 87]
"""""
# Accessing elements of the list
print("First element: ", numbers[0])
print("Last element: ", numbers[-1])
print(numbers)

# Slicing the list
print("Slice[1:4]", numbers[1:4])
print("Slice[:3]", numbers[:3])
print("Slice[2:]", numbers[2:])


# Modifying elements of the list
#numbers[0] = 15
#numbers[-1] = 99

# Adding elements to the end of the list
numbers.append(73)
numbers.append(99)
print(numbers)


# Removing elements of the list
removed_element = numbers.pop(3)
print("Removed element:", removed_element)
print(numbers)
"""""

# Length of the list
list_length = len(numbers)
print("Length of the list: ", list_length)


# Looping through the list
for num in numbers:
    print(num)
