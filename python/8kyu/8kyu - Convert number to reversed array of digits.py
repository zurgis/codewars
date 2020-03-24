# Convert number to reversed array of digits
# Given a random number:

# C#: long;
# C++: unsigned long;
# You have to return the digits of this number within an array in reverse order.

# Example:
# 348597 => [7,9,5,8,4,3]

# Best Practices
def digitize(n):
    return list(map(int, str(n)[::-1]))

# My answer
def digitize(n):
    return [int(n) for n in str(n)[::-1]]