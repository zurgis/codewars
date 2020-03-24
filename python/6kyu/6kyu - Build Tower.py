# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Ruby: returns an Array;
# Have fun!

# for example, a tower of 3 floors looks like below

# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
# and a tower of 6 floors looks like below

# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]
# Go challenge Build Tower Advanced once you have finished this :)

# Best Practices
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# My answer
def tower_builder(n_floors):
    tower = []
    x = 1
    for i in range(n_floors - 1, -1, -1):
        block = ' ' * i
        for j in range(x):
            block += '*'
        block += ' ' * i 
        tower.append(block)
        x += 2
    return tower