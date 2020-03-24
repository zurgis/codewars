# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

# Best Practices
def merge_arrays(first, second): 
    return sorted(set(first + second))

# My answer
def merge_arrays(first, second):
    return sorted(list(set(first).union(second)))