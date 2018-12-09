class Student(object):
    pass
s = Student()
s.name = 'Michael'
s.name

# bind method to a instance
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age
print(hasattr(s,'set_age'))
ss = Student()
print(hasattr(ss, 'set_age')) # false, not to s instance

# bind method to a class
def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(100)
ss.set_score(101)
s.score
ss.score

# what can we do if we want to constrain the attribute in a class
class Student(object):
    __slots__ = ('name','age')
s = Student()
# s.score = 100 error
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 23 # pass
class GraduateStudent(Student):
    __slots__ = ('name')
    pass
g = GraduateStudent()

g.age = 34 # pass
'''
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
