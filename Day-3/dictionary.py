# Creating a dictionary

student = {
    "name": "Alice",
    "age": "20",
    "major": "Computer science",
    "gpa": "3.8"
}

# Accessing values in the dictionary
print("Name:", student["name"])
print("Age:", student["age"])

# Modifying Values in the dictionary
student["gpa"] = 4.0
print("gpa:", student["gpa"])

# Adding a new key value pair in dictionary
student["University"] = "ABC University"

# Checking if a key exists in the dictionary
print("Is 'major' in the dictionary?", "major" in student)
print("Is 'grade' in the dictionary?", "grade" in student)

# length of the dictionary
print("Length of the dictionary is: ", len(student))

# Looping through dictionary keys
print("Dictionary Keys:")
for key in student:
    print (key)

# Looping through dictionary's values
print("Dictionary Values:")
for value in student.values():
    print(value)

# Looping through both keys and values
for key, value in student.items():
    print(key, ":", value)
