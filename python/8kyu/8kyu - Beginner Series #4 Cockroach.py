# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

# For example:

# cockroach_speed(1.08) == 30
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

# Best Practices
def cockroach_speed(s):
    return s // 0.036

# My answer
def cockroach_speed(s):
    import math
    return math.floor(s * 27.778)