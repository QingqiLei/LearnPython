from io import StringIO
import sys
f = StringIO()
f.write('hello')
f.write(' ')
f.write("world!")
print(f.getvalue(), sep=' ', end='n', file=sys.stdout, flush=False)
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
