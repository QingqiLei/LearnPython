d = {"t1":1,"t2":2,"t3":3}
for key in d: # key
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)
from collections import Iterable
isinstance("acb",Iterable)
isinstance(123,Iterable)

for i, value in enumerate(['a','b','c']):
    print(i,value)
for x,y in [[1,2],[3,4],[5,6]]:
    print(x,y)
def findMinAndMax(L:tuple):
    min = L[0]
    max = L[0]
    for i in L:
        if i>max:
            max =i 
        if i< min:
            min = i
    print('min =',min, 'max = ',max)
    return min, max
findMinAndMax((1,2,0,4,5,6,7,8))
