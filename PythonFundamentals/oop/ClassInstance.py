# all object extends object
class Student(object):
    pass

bart = Student()
id(bart)
bart.name = 'wang' # we can bing variable at our will
bart.age = 15
class Student(object):
    def __init__(self, name, score): # with this existance, we need to input parameter when create new Student
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s'% (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else: return 'C'
    pass
bart = Student('wang',19) # __init__() missing 2 required positional arguments: 'name' and 'score'
print(bart.name)
bart.print_score()
bart.get_grade()
