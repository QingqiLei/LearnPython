# built-in functions: http://docs.python.org/3/library/functions.html#abs


print(abs(-100))
try:
    abs(1,2)
except TypeError as e:
    print(e)

print(int('123'))
print(float(12))
print(str(12))
print(bool(34))
print(bool(0))
print(bool("df"))
print(bool(""))

print(hex(123))
