# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

# Example
# divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

# Best Practices
def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]

# My answer
def divisible_by(numbers, divisor):
    return list(filter(lambda numbers: (numbers % divisor) == 0, numbers))