def lazy_sum(* args): # args is a tuple, tuple is not
    def sum():
        ax = 0
        print(type(args))
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5)
f
f() # call f function
'''
sum() is the inner function of lazy_sum(), and inner function sum() can
use the parameter of lazy_sum(), and when lazy_sum() returns sum(), the variables
have alway already stored in sum().
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
f1()
f2()
f3()

def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s+1
        return s
    return counter


def createCounter():
    m = [0]
    def counter():
        m[0] = m[0] +  1
        return m[0]
    return counter

counterB = createCounter()
[counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]

list = [1,2]     # the mutability of string and list
string = "11111"
def get(L,string):
    L.append(12)
    print(id(L))
    string1 = string
    string= "234234"
    print(id(string1))
print(id(list),id(string),get(list,string))
print(list, string) # list is changed, string is not
