# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

# For example n = 3 result in "I\n I\n I", or printed:

# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:

# I
#  I
#   I
#    I
#     I
#      I
#       I

# Best Practices
def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))

# My answer
def draw_stairs(n):
    A = ''
    for i in range(n):
        if i == n - 1:
            A += (' ' * i + 'I')          
        else:
            A += (' ' * i + 'I\n')
    return A