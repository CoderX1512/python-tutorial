"""
# Specify the file path and name
file_path = "C:/Users/VMUser/Documents/example.txt"

# Open the file in write mode and write content
with open(file_path, "w") as file:
    file.write("Hello, this is content written to a file in your laptop. ")

#print("File created and content written successfully.")


# Open a file in read mode and print each line
with open("C:/Users/VMUser/Documents/example.txt", "r") as file:
    for line in file:
        print(line.strip()) # Removes newline characters


# open a file in append mode and add new content
with open("C:/Users/VMUser/Documents/example.txt", "a") as file:
    file.write("\nThis is additional content appended to the file.")

# open a file in read mode
with open("C:/Users/VMUser/Documents/example.txt", "r") as file:
    print(file.read())



import csv

# Writing data to a csv file
data = [["Name", "Age"], ["Alice", 22], ["Bob", 30]]
with open("C:/Users/VMUser/Documents/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading data from a CSV file
with open("C:/Users/VMUser/Documents/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""

import json
# Writing data to a JSON file
data = {"name": "Alice", "Age": 22, "city": "New York"}
with open("C:/Users/VMUser/Documents/data.json", "w") as file:
    json.dump(data, file)

# Reading data from a JSON file
with open("C:/Users/VMUser/Documents/data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)


