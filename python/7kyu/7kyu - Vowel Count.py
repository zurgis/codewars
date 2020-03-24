# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

# The input string will only consist of lower case letters and/or spaces.

# Best Practices
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# My answer
def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels += 1
    return num_vowels