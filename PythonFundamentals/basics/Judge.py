# if
age = 3
if age >=18:
    print('your age is', age)
    print('adult')
elif age > 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')
list = []
if list:
    print(list) # if age != 0 or String or list length != 0

birth = input('birth: ')
try:
    birth = int(birth)
except Exception as e:
    print(e)
    quit(-1)

if birth < 2000:
    print('before 00')
else:
    print('after 00')