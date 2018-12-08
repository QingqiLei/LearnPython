# list, tuple, dict, set, str are available for for statement
# Iterable object can use for
from collections import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance([x for x in range(10)], Iterable)
isinstance(100, Iterable)

from collections import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance('abc', Iterator)

isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

for x in [1,2,3,4,5]:
    pass
it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
        pass
    except StopIteration:
        break
