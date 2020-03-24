# Wilson primes satisfy the following condition. Let P represent a prime number.

# Then ((P-1)! + 1) / (P * P) should give a whole number.

# Your task is to create a function that returns true if the given number is a Wilson prime.

def am_i_wilson(n):
    return n in (5, 13, 563)

'''
    import math
    if n < 2 or not all(n % i for i in range(2, n)):
        return False
    return (math.factorial(n - 1) + 1) % (n ** 2) == 0
'''