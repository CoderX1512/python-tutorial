# Program to copy the content of one file to another
file_path1 = "C:/Users/VMUser/Documents/original.txt"
"""
with open(file_path, "w") as file:
    file.write("This is the original file content!")

print("File successfully created.")

"""
file_path2 = "C:/Users/VMUser/Documents/copy.txt"
# first method

# open both files
with open(file_path1, 'r') as firstfile, open(file_path2, 'w') as secondfile:
    # read content from first file
    for line in firstfile:
        # write content to second file
        secondfile.write(line)
print("File content successfully copied.")
# second method
with open(file_path1, 'r') as firstfile, open(file_path2, 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)

# third method
# import module
import shutil

# use copyfile()
shutil.copyfile(file_path1, file_path2)
