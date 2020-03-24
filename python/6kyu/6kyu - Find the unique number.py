# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique

# Best Practices
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# My answer
def find_uniq(arr):
    arr.sort()
    n = arr[0]
    if (n < arr[len(arr) - 1]) and (n < arr[len(arr) - 2]):
        return n
    else:
        return arr[len(arr) - 1]   # n: unique integer in the array