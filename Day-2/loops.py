# print from 1 to 5
for num in range(1, 6):
    print(num)

# print using while loop from 1 to 5

num = 1
while num <= 5:
    print(num)
    num += 1

# Using a for loop for a list comprehension to calculate squares of numbers


numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Squares:", squares)

# Using a while loop to continuously prompt the user for input until quit is entered

user_input = ''
while user_input != 'quit':
    user_input = input("Enter a command('quit' to exit):")
    print("You entered:", user_input)

# code to print odd even for the numbers 1 to 20
# method-1
# number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = []
for i in range(1, 21):
    number.append(i)
# print(number)

for num in number:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

# method-2
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
