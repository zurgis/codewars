# Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

# You need to consider the following ratings:

# Terrible: tip 0%
# Poor: tip 5%
# Good: tip 10%
# Great: tip 15%
# Excellent: tip 20%
# The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

# "Rating not recognised" in Javascript, Python and Ruby...
# ...or null in Java
# ...or -1 in C#
# Because you're a nice person, you always round up the tip, regardless of the service.

def calculate_tip(amount, rating):
    import math
    a = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}
    if rating.lower() in a:
        return math.ceil(amount * a[rating.lower()] / 100)
    return 'Rating not recognised'