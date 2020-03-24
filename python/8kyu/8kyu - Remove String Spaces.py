# Simple, remove the spaces from the string, then return the resultant string.

# Best Practices
def no_space(x):
    return x.replace(' ', '')

# My answer
def no_space(x):
    return ''.join(x.split())