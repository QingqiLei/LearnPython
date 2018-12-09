int('12345', base=8)
int('12345',8)
int('10101010110',base = 2)
int('10101010',2)
def int2(x,base = 2):
    return int(x, base)

import functools
int2 = functools.partial(int, base = 2) # return a new function
int2('001010101010')
int2('01010101',base = 10)
# *args : ('2', **kw), **kw: (*args, base = 2)
max2 = functools.partial(max, 10)
max2(1,2,3)
