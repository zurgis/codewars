# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

# Best Practices
def sum_mix(arr):
    return sum(map(int, arr))

# My answer
def sum_mix(arr):
    return sum([int(i) for i in arr])