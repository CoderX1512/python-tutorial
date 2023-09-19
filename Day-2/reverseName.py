"""
first_name = str(input("Enter the first name: "))
last_name = str(input("Enter the second name: "))
print(last_name, first_name)
"""

# function to reverse the first and last name


def rev_name():
    name = str(input("Enter the name: ")).split()
    print(name[len(name)-1], name[0])
