word = 'madam'


# rev_word = word[::-1]
# print(rev_word)


def checkPallindrome(word):
    if (word == word[::-1]):
        print("Yes it is a palindrome")
    else:
        print("Its not a palindrome")


checkPallindrome(word)
