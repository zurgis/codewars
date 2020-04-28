# In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
# Your task is to return a new sequence of dimensions, sorted ascending by area.

# For example,

# seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
# sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
# This kata inspired by Sort rectangles and circles by area.

seq = [(4.23, 6.43), 1.23, 3.444, (1.342, 3.212)]
print(seq)
#floats = [i for i in seq if type(i) != tuple]
#tuples = [i for i in seq if type(i) == tuple]
#print(sorted(tuples) + sorted(floats))
#print(sorted(seq, key=map((lambda x: x ** 2) for x in seq if type(x) == float else (lambda x, y: x * y), seq)))
#a = sorted([i for i in seq if type(i) == float])
print(sorted(seq, key=lambda x: x[0] if type(x) == tuple else x**2)) # - Проходит 152 теста и 53 нет

a = sorted(seq, key=lambda x: x[0]*x[1] if type(x) == tuple else x**2)
#print(sorted(a, key=lambda x: x[0]*x[1] if type(x) == tuple else x**2))
#print(list(filter(lambda x: x[0] if type(x) == tuple else x, a)))
print(a)
b = []
c = None
for i in seq:
    c = i


    ###### НАПИСАТЬ
    
