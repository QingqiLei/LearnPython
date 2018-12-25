import threading
local_school = threading.local()
def process_student():
    std = local_school:student
