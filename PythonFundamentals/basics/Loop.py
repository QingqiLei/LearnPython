# In python, there two kinds of loop, for in and while
# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for i in list(range(5)):
    sum  += i
print(sum)

# while
sum = 0
n = 99
while n > 0:
    sum = sum +n
    n -= 2
    if n < 10:
        if n < 11:
            continue
        break # break the while
i = 0
j = 0
while i < 10:
    i = i+1
    while j < 10:
        j = j+1
        if j == 5:
            print('break')
            break
print(i, j)
print(sum)
