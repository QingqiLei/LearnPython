[x * x for x in range(1,11)]
[x * x for x in range(1,11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']
import os
[d for d in os.listdir('C:///\\/\\\\//')]
L = {'x':'A', 'y':'B','z':'C'}
[k + '=' + v for k, v in L.items()]
print((k + '=' + v for k, v in L.items()))
L = [1,'Hello','World','IBM',5]
[s.lower() for s in L if isinstance(s,str) ]
