class Student(object):
    name = 'student'
    count = 0
    def __init__(self, name):
        Student.count +=1
        self.name = name

s = Student('Bob')
s.score = 90
Student.name
Student.count
