def is_odd(n):
    return n%2 == 1 # is n % 2 == 1, n is valid
list(filter(is_odd, [1,2,3,4,5,6])) # is_odd, no parameter

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['a',' ','b','C ',None]))
print(list(filter(not_empty, ['a',' ','b','C ',None])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0 # what's x?

def primes():
    yield 2
    it = _odd_iter()
    print(it)  # generator
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
for n in primes(): # primes() is a generator
    if n < 100:
        print(n)
    else:
        break
print(type(primes()))
def is_palindrome(n):
    n = str(n)
    m = n[::-1]
    return n==m

def is_palindrome(n):
    temp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n = n //10
    return rev == temp
is_palindrome(111)
output = filter(is_palindrome, range(1,100))
print(list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('pass!')
else:
    print('filled!')
