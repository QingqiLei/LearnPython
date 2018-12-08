d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# dictionary
# only one value
# Error if key doesn't exist
# the key must be immutable, list is mutable, so list object can not be key

print(d.get('ttt', "df"))
print(d.pop('Bob'))
print(d)


print('----------')
# set
s = set([1,1,1,1,2,3,3,3])
print(s)

s.remove( 1)
t = set([3,4,5])
print(s & t)
print(s | t)

print('----------')
# and let's talk about immutable object
# only list is immutable
a = 'immutable'
b = a.replace('a','T')
print(a)
print(b)