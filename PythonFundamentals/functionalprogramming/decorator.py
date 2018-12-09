import functools
def log(func):
    def wrapper(*args, **kw): # can take any parameter
        print('call %s():' % func.__name__) # output the log
        return func(*args, **kw) # call the func
    return wrapper


@log
def now():
    print('2015-3-25')
now() # equivalent to now = log(now)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def now():
    print("2018-9-19")
now() # now = log('execute')(now) ,==decorator(now), return wrapper
print(now.__name__)
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print('1028')
now()
print(now.__name__)

import time
def printRunTime(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        start = time.time()
        res = fun(*args, **kw)
        end = time.time()
        print("%s execute time = %d ms!"% ( fun.__name__, (end - start)*1000))
        return res
    return wrapper
@printRunTime
def print1():
    time.sleep(2)
    print(1)
print1()
