# This series of katas will introduce you to basics of doing geometry with computers.

# Vector objects have x, y, and z attributes.

# Write a function calculating dot product of Vector a and Vector b.

# You can read more about dot product on Wikipedia.

# Tests round answers to 6 decimal places

# Best Practices
def dot_product(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

# My answer
def dot_product(a, b):
    return sum([a.x * b.x, a.y * b.y, a.z * b.z])