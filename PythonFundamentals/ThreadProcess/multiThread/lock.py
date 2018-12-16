import time, threading
import sys
balance = 0
def change_it(n):
    global balance
    balance = balance +n
    balance = balance -n
def run_thread(n):
    for i in range(190000):
        change_it(n)
t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance, sep=' ', end='n', file=sys.stdout, flush=False)
# balance = balance + n   =>
# x = balance + n
# balance = x
lock = threading.Lock()
def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
