# using type(), we can get the type of a class ,
# also can create a new class
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s.'%name)
def fn(self, name='world'): # firstly, define a method
    print('Hello,fn, %s.' % name)
Hello = type('Hello,type(),',(object,),dict(hello=fn)) # create a new class
h = Hello()
h.hello()
h.__class__

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self, value:self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
    pass
L = MyList()
L.add(1)
L
#def
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):

    def __init__(self, name):


        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases,attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s == %s'%(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name # a property
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key): # a method
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# (创建一个实例：)
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
u.__getattr__('id')
u.__table__

# when create an instance of User(Model), python find metaclass in User firstly,
# if not found, then find it in super class(Model),so using the ModelMeraclass defined in Model
'''
using ModelMeraclass
1. don't have to modify the Model class
2. store the field in class's room, and delete the property in instanceselfself.
     because the instance property will hide the class property with the same name

'''
