import pickle
import os
d = dict(name = 'Bob', age = 20, score = 99)
pickle.dumps(d)
f = open('dump.txt','wb')  # open a file
pickle.dump(d,f) # write
f.close() # close, otherwise, the content wasn't written
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
d
os.remove('dump.txt')

import json
d = dict(name = 'Bob', age = 'age', score = 88)
json.dumps(d, ensure_ascii=True)
type(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name;
        self.age = age
        self.score = score
s = Student('BOb',20,98)
def student2dict(std):
    return {
    'name': std.name,
    'age': std.age,
    'score': std.score
    }
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
