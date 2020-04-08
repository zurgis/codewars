# Given a string of characters, I want the function findMiddle()/find_middle() to return the middle number in the product of each digit in the string.

# Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

# Not all strings will contain digits. In this case and the case for any non-strings, return -1.

# If the product has an even number of digits, return the middle two digits

# Example: 1563 -> 56

# NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1

# Best Practices
from operator import mul
from functools import reduce

def find_middle(s):
    if not s or not isinstance(s,str): return -1
    
    lstDig = [int(c) for c in s if c.isnumeric()]
    if not lstDig: return -1
    
    prod = str( reduce(mul,lstDig) )
    i    = (len(prod) - 1) // 2
    return int(prod[i:-i or len(prod)])

# My answer
def find_middle(string):
    from functools import reduce
    if type(string) is str:
        list_numbers = [int(i) for i in string if i.isdigit()]
        if not list_numbers:
            return -1
            
        number = str(reduce(lambda x, y: x * y, list_numbers))
        index = len(number) // 2
        return int(number[index]) if len(number) % 2 == 1 else int(number[index-1:index+1])
    return -1

def find_middle(string):
    if type(string) is str:
        a = 1
        num = [int(i) for i in string if i.isdigit()]
        if not num:
            return -1
        for i in num:
            a *= i
        a = str(a)
        return int(a[len(a)//2]) if len(a) % 2 == 1 else int(a[(len(a)//2)-1:(len(a)//2)+1])
    return -1