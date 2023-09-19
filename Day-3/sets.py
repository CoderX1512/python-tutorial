# Creating a set(unordered collection) of fruits
fruits = {"apple", "banana", "orange"}
print(fruits)

# Adding an element to the set
fruits.add("grape")
print(fruits)

# Removing an element from the set
fruits.remove("banana")
print(fruits)

# Checking if an element is in the set
print("Is apple in the set? ", "apple" in fruits)
print("Is banana in the set? ", "banana" in fruits)

# Length of the sets
print("Length of the set is:", len(fruits))

# Looping through the set
print("set elements:")
for fruit in fruits:
    print(fruit)
