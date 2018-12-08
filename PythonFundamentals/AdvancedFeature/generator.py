L = [x * x for x in range(10)]
g = (x * x for x in range(10)) # store the algorithem
next(g)

def fib(max):
    a,b = 0,1
    while b < max:
        print(b)
        a,b = b, a+b
    return 'done'
fib(45)

def fib(max):
    a,b = 0,1
    while b < max:
        yield b  # returns
        a,b = b, a+b
    return 'done'
g = fib(45)
next(g)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
g = odd()
next(g)

for n in fib(55): #  mostly, we use for rather than next()
    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break;

def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

def triangles():
    L = [1]
    while True:
        yield L
        L = [sum (i) for i in zip([0] + L, L + [0])]

g = triangles()
print(next(g))

L = [1,2,3,4]
L = zip([0] + L, L + [0])
for i in L:
    print(type(i))
