type(123)
type("str")
type(None)
type([]) == type([])
type(())
type([])
import types
type(lambda x:x) == types.LambdaType
type(abs) == types.BuiltinFunctionType
type((x for x in range(10))) == types.GeneratorType
# type() and instance() have the same feature
import extends
dir('extends.Dog')
print(234234)
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Animal("Husky",1)
hasattr(dog1,'name')
hasattr(dog1, 'y')
setattr(dog1, 'name','dog')
getattr(dog1,'name')
setattr(dog1, 'ttt','ttt')
getattr(dog1,'ttt')
getattr(dog1,'hello','wangwang') # with default value

def readData():
    print('read image data...')
def readImage(fp):  # make sure fp object has readData() method
    if hasattr(fp,'read'):
        return readData(fp)
    return None
