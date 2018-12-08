# list
classmates = ['Michael', 'Bob', 'Tracy']  # mutable
print(len(classmates))


print(classmates[-1], classmates[-2], classmates[-3])
classmates.append('Adam')
classmates.insert(0, 'Jack')
print(classmates)
classmates.sort()
print(classmates)
classmates.pop(0)

print(classmates)
classmates[-1] = 'Hello'
print(classmates)
L = ['appne', 123, True]
classmates[-1] = L
print(classmates, len(classmates))

# tuple
classmates = 'Michael', 'Bob', [1,2,3]  # immutable
t = (1,)
print(type(t))
t=(1)
print(type(t))
classmates[2].append(55555)
print(classmates)


