def fact(n):
    if n==1:
        return 1
    if(n < 0):
        return
    return n * fact(n -1)
print(fact(10))
print(fact(-1))

def hanoi(n,a,b,c):
    if n==1:
        print(a, '-->',c) # from a to c
    else:
        hanoi(n-1,a,c,b) # from a to b
        print(a, '-->',c)
        hanoi(n-1,b,a,c) # from b to c
hanoi(3,'A','B','C')
