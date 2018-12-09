list(map(lambda x: x * x, [1,2,3,4,5,6]))
'''
lambda x:x *x    is
def f(x):
    return x*x

anonymous function is a expression equation,
the advanteges of anonymous function is that it doesn't have name,
so no conflict of names

'''
def is_odd(n):
    return n%2 == 1
list(filter(is_odd, range(1,20)))
list(filter(lambda x: x%2 == 1, range(1,20)))
