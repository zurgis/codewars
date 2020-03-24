# Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.

# If you need help, here's a reference:

# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# Best Practices
def take(arr,n):
    return arr[:n]

# My answer
def take(arr,n):
    return [arr[i] for i in range(n) if i < len(arr)]