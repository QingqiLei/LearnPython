from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>',member, ',',member.value)
from enum import unique
@unique
class WeekDay(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
WeekDay.Mon
type(WeekDay.Thu)
type(WeekDay(5))

class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('bart',Gender.Male)
if bart.gender == Gender.Male:
    print("pass")
else:
    print('failed')
