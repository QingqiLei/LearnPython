def f(x):
    return x*x
r = map(f, [1,2,3,4,5,6]) # apply f to every element in [] or ()
print(type(r)) # <class 'map'>

list(r)
list(map(str, (1,2,3,4,4)))
list(map(str, [1,2,3,4]))
from functools import reduce
def add(x , y):
    return x*10+y
reduce(add, [1,2,3,4,5,6])  # good, I understand

def fn(x,y):
    return x*10+y
def char2num(s,t):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    print(ord(s) - ord(t))
    return digits.get(str(ord(s) - ord(t)), -1)
reduce(fn, map(char2num, '12345','00000')) # map(int, args) map(int)
