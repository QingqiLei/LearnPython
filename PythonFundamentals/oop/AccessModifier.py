class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def set_score(self,score):
        if 0<= score <= 100:
            self.__score =score
        else:
            raise ValueError("bad score")
bart = Student('wang',16)
# bart.__name  we can not access it
bart._Student__name
bart.__name = "li" # inside the class, the __name has already become _Student__name
bart.print_score()

bart.__name
