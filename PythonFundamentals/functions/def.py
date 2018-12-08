def nop(age):
    if age >= 18:
        pass  # do nothing

    print(age)

i = 10
while( i < 30):
    nop(i)
    i +=1

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operator type")
    if x >=0:
        return x
    else:
        return -x

import math
def move ( x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny # return a tuple
print(move(100, 100 , 60 ,math.pi /3 ))

import numpy as np
def quadratic(a,b,c):
    if a==0:
        raise TypeError(" a can not be 0")
    if not isinstance(a,(int, float)) or not isinstance(b,(int, float))or not isinstance(c,(int, float)):
        raise TypeError("bad operand type")
    delta = math.pow(b,2) - 4*a * c
    if delta == 0:
        print("x=%.2f"%x)
        return -b/(2*a)
    elif delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+ math.sqrt(delta))/(2*a)
        print("x1 = %.2f,x2= %.2f"%(x1,x2))
        return x1,x2
    elif delta < 0:
        x1 = (-b + complex(0,1) * math.sqrt(-1* delta))/(2*a)
        x2 = (-b - complex(0,1) * math.sqrt((-1) * delta))/(2*a)
        print(x1,x2)
        return x1,x2
quadratic(1,3,1)
quadratic(1,2,3)
