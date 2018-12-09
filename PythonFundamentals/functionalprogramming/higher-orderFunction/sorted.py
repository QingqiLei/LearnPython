sorted([4,3,5,7,4,5,6,1,3,6,8])
sorted([36,5,-12,9,-21], key = abs)
sorted(['Bob','about','Zoo','Credit']) # capitalization, uppercase
sorted(['Bob','about','Zoo','Credit'], key = str.lower)
sorted([1,-2,3,-4,5,-6],key = abs, reverse = True)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L, key = by_name))

def by_score(t):
    return t[1]
print(sorted(L, key = by_score,reverse = True))
