class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self): #
        return "Student object(name: %s)"% self.name
    __repr__ = __str__
s = Student("Michael")
print(Student('Michael'))
s # if we don't deal with __repr__, this will display merry index

class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    def __iter__(self):
        return self # return itself
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)
class Fib(object): # make Fib() like a list,
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1,1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
f = Fib()
f[7]
f[0:10]
f[:10:2] # I didn't deal with the step

class Student(object):
    def __init__(self):
        self.name = "Michael"
    def __getattr__(self, attr):
        # return 'doesn\'t exist'
        if attr == 'age':
            return lambda : 25

s = Student()
s.score # doesn't exist
s.score = 90
s.score # 90
print(s.abc) # None
s.height()
s.age()
s.hright()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s' %self.name)
s = Student('Michael')
s()
callable(Student("1"))
callable(max)
callable([1,2,3,4])
callable(['str'])
callable(None)
