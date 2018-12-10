class Student(object):

    @property
    def score(self):
        return self._score # one underscore
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value
s = Student()
s.score = 60
s.score

class Student(object):
    @property
    def birth(self):           # read
        return self._birth
    @birth.setter              # write
    def birth(self,value):
        self._birth = value
    @property                  # read
    def age(self):
        return 2015 - self._birth
# birth: read and write, age: read, the attribute exists if there is its setter
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater than 0")
        self._width = value

    @property
    def height(self):
        return self.height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self._height = value
    @property
    def resolution(self):
        return self._height * self._width
s = Screen()
s.width = 1024
s.height = 100
print(s.resolution)
