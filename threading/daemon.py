""" Daemon Threads:
    Suppose there's a long running task, reading log files. The user has to get alerts when error is encountered!

    A daemon thread can be used which will alert the user without affecting the normal exec.
"""

import threading
import time

path = "text.txt"
text = ""


def read_file():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)


def print_print():
    for i in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_print)

t1.start()
t2.start()
