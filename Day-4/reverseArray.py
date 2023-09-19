#logic 1

array = [1, 2, 3, 4, 5, 6, 7]
print(array[::-1])

#logic 2

array2 = list()
i = len(array) - 1
while i >= 0:
    array2.append(array.pop(i))
    i = i -1
print(array2)