import os
os.name
os.uname()
os.environ
os.environ.get('PATH')
os.path.abspath('.')
path = os.path.join('/usr/local/PythonCode/LearnPython/PythonFundamentals','testdir')
os.mkdir(path)
os.rmdir(path)
# return the parent path and the file
os.path.split('/Users/michael/testdir/file.txt')
os.path.splitext('/Users/michael/testdir/file.txt')
os.mkdir('test.txt')


os.rename('test.txt','test')
os.rmdir('test')
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('/usr/local/PythonCode/LearnPython/PythonFundamentals/IO/') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
[x for x in os.listdir('/usr/local/PythonCode/LearnPython/PythonFundamentals/IO/') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
os.listdir('/usr/local/PythonCode/LearnPython/PythonFundamentals/IO')
