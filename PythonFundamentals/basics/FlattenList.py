import sys
import itertools
import functools
import operator
list = [[1, 2, [100,200]], [4, 5, 6], [7], [8, 9]]
print([item for sublist in list for item in sublist])

print(sum(list,[]))

print(functools.reduce(operator.iconcat, list, []))
print(functools.reduce(lambda x,y: x+y, list))
print(functools.reduce(operator.concat,list))
