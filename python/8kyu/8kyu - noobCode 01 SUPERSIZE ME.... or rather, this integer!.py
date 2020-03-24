# Write a function that rearranges an integer into its largest possible value.

# super_size(123456) # 654321
# super_size(105)    # 510
# super_size(12)     # 21
# If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.

# Best Practices
def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))

# My answer
def super_size(n):
    x = sorted([n for n in str(n)], reverse=True)
    n = ''.join(x)
    return int(n)