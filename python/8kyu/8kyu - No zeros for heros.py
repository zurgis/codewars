# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

# Best Practices
def no_boring_zeros(n):
    return int(str(n).rstrip('0')) if n else n

# My answer
def no_boring_zeros(n):
    x = str(n)
    if n == 0:
        return 0
    else:
        while x[-1] == '0':
            x = x[:-1]
        return int(x)