
sentence = str(input("Enter the sentence: "))
words = sentence.split()
print("No. of words:", len(words))

count = 0
for word in words:
    count += len(word)

print("No of letters:", count)



