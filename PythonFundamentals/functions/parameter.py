def power(x, n = 2):
    res = 1
    while(n > 0):
        n -=1
        res = res * x
    return res
power(5,5)

def add_end(L = []):
    L.append("end")
    return L
add_end([1,2,3])
add_end()
print(add_end())
print(add_end())
print(add_end())

def add_end(t,L = None):  # None is immutable, list is mutable
    if L is None:
        L = []
    L.append("end")
    return L
add_end(6,[])

'''
def person(a,b), are positional parameter
def person(c = None, d = "w") is optional parameter
def person(*,r = 'W'，tt = 'oo') is keyword parameter with default value
def person(**r) is keyword parameter


'''
def person(**name):
    print(name)
person(nam = 'www',age = 14)

def calc (*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
calc(1,2,3,4,5,56) # 3191
calc() # 0
def string(*string):
    print(type(string))
string('abcdefg') # tuple
print(type('abcdefg')) # str


nums = [1,2,3,4,5]
# calc(nums)  error
calc(nums[0],nums[1],nums[2],nums[3],nums[4])
calc(*nums)

def person(name, age, **kw):
    print('name:', name, 'age:',age,'other:',kw)
person('Michael',30)
person('Bob',35,city='Shanghai',sex = 'male')
dics = {'city':'Beijing','job':'Engineer'}
person('lei',15,**dics)

# city and job are keyword argument, name and age are positional argument.
# * lets city and job be keyword argument
def person(name, age, * , city, job): # city and job are required
    print(name, age, city, job)  # must input the name of parameter explicitly
person("lei",26,city="Shanghai", job=  "IT") #

def person(name, age, * , city = "Shanghai", job): #  city is not required
    print(name, age, city, job)
person("lei",25,job = "IT")

def person ( name, age , *list, city, job = 'IT'): # city and job are keyword argument
    print(name, age, city, job)
L = [1,2,3,4]
person("lei",15,L, city = "Shanghai")
person("lei",14,city = 'Shanghai')
def person(name, age, city, job):
    print(name, age, city, job)
person(name = "lei",age = 14,city = 'Shanghai',job = 'IT')
# person(name = "lei",age = 15, 'Shanghai','IT') error

def f1(a, b, c = 0, * args, ** kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw): # d is a keyword argument, and kw represent a dics,
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
f1(1,2)
f1(1,2,c=123)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2, d = 99, ext = None)
args = (2,3)
kw = {"d":"dddd","t2":"t2t2t2"}
f1(*args,**kw)# !!!!!!!!!!
f2(*args,**kw)
# f2(1,2,3,4,5,6,7,8,d = "d") # f2() takes from 2 to 3 positional arguments but 8 positional was given
def product(*t):
    if(len(t) ==0):
        raise TypeError
    print(len(t))
    sum = 1
    for i in t:
        sum = sum * i
    return sum

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
if product(5, 6) != 30:
    print('测试失败!')
if product(5, 6, 7) != 210:
    print('测试失败!')
if product(5, 6, 7, 9) != 1890:
    print('测试失败!')

try:
    product()
    print("failed")
except TypeError:
    print('pass!')
