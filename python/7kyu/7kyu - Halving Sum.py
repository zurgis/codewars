# Task
# Given a positive integer n, calculate the following sum:

# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.

# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47

def halving_sum(n):
    sum = 0
    while n > 1:
        sum += n
        n //= 2 
    return sum + 1

''' 
    return n and n + halving_sum(n >> 1)
    return n if n == 1 else n + halving_sum(n // 2)
    return n and n + halving_sum(n // 2)
'''