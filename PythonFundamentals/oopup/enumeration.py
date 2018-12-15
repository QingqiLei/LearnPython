from enum import Enum
# object in enumeration is singleton object
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(324)
for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
for enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Mon)

print(Weekday['Sun'])
print(Weekday.Tue.value)
print(Weekday(1))
print(Weekday(1) == Weekday['Mon'])
for name, member in Weekday.__members__.items():
    print(name,'=>',member)
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart',Gender.Male)
print(bart.gender == Gender.Male)
