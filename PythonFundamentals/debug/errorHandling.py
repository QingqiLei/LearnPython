def foo():
    r = some_function()
    if r ==(-1):
        return -1
    pass
    return r
def bar():
    r = foo()
    if r == (-1):
        print('error')
    else:
        pass
import logging
try:
    print('try...')
    r = 10/0
    print('result')
except ValueError as e:
    print('ValueError:', e)
    logging.exception(e)
except ZeroDivisionError as e:
    print('except: ',e)
    logging.exception(e)
else:
    print('no error')
finally:        # will run anyway
    print("finally")
    print()

class MyError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise MyError('invalid value: %s'%s)
    return 10/n
foo('0')
