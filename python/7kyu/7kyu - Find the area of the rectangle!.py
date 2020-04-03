# Find the area of a rectangle when provided with one diagonal and one side of the rectangle. If the input diagonal is less than or equal to the length of the side, return "Not a rectangle". If the resultant area has decimals round it to two places.

# This kata is meant for beginners. Rank and upvote to bring it out of beta!

def area(d, l): 
    import math
    w = d ** 2 - l ** 2
    return round(l * math.sqrt(w), 2) if d > l else 'Not a rectangle'