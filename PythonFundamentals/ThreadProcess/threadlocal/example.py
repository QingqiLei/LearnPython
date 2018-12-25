import sys

def do_subtask_1(std):
    print("do_subtask_1 ",std.name, sep=' ', end='n', file=sys.stdout, flush=False)
def do_subtask_2(std):
    print("do_subtask_2 ",std.name, sep=' ', end='n', file=sys.stdout, flush=False)
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)
def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
class Student(object):
    def __init__(self, name):
        self.name = name
def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)

process_student("zhao")
