# _thread and threading , threading is high than _thread
import time, threading
import sys
def loop():
    print('thread %s is running...'%threading.current_thread().name, sep=' ', end='n', file=sys.stdout, flush=False)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s'%(threading.current_thread().name, n ), sep=' ', end='n', file=sys.stdout, flush=False)
        time.sleep(1)
    print('thread %s ended.'%threading.current_thread().name, sep=' ', end='n', file=sys.stdout, flush=False)
print('thread %s is running'%(threading.current_thread().name), sep=' ', end='n', file=sys.stdout, flush=False)
# define a thread
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name, sep=' ', end='n', file=sys.stdout, flush=False)
# MainThread is the default thread,
