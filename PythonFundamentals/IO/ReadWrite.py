f = open('/usr/local/PythonCode/LearnPython/learning.py','r')
f.read()
f.close
try:
    f = open('/usr/local/PythonCode/LearnPython/learning.py','r')
    print(f.read())
finally:
    if f:
        f.close()
# using with, don't have to close
with open('/usr/local/PythonCode/LearnPython/learning.py','r') as f:
    for line in f.readline():
        print(line.strip())
    print(f.read())
f = open('/home/chauncey/Downloads/po.mp4','rb')
f.read()
f.close
f= open('/usr/local/PythonCode/LearnPython/1.txt','w')
f.write('Hello, world!')
f.close()
with open('/usr/local/PythonCode/LearnPython/1.txt','a') as f:
    f.write('fewfsadfasddfe')
