# Write a function that always returns 5

# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

# Good luck :)

# Best Practices
def unusual_five():
    return len('five!')

# My answer
def unusual_five():
    a = 'abcdef'
    return a.index('f')