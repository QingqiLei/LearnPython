def f(x):
    return x*x
r = map(f, [1,2,3,4,5,6]) # apply f to every element in [] or ()
print(type(r)) # <class 'map'>

# the iterable arguments may be a sequences or any iterable object, the result is also a list
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
    return digits.get(str(ord(s) - ord(t)), -1)
reduce(fn, map(char2num, '12345','000')) # map(int, args) map(int)


digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num,s))
str2int('123456')

# lambda
def char2num2(s):
    return digits.get(s,-1)
def str2int(s):
    return reduce(lambda x,y:x *10 + y, map(char2num2, s))
str2int('45678f')

def normalize(name:str):
    return name[0].upper() + name[1:].lower()
L1 = ['adam','LIST','barI']
list(map(normalize, L1))
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f, L)
prod([1,2,3,4])

def str2float(s):
    nums = map(lambda ch: digits[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums)
print(str2float('120.002'))
