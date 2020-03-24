# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

#   sumStr("4", "5")    // should output "9"
#   sumStr("34", "5")   // should output "39"
# If either input is an empty string, consider it as zero.

# Best Practices
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

# My answer
def sum_str(a, b):
    if a == '':
        a = 0
    if b == '':
        b = 0
    return str(int(a) + int(b))