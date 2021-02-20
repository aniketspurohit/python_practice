""" This particular py file demonstrates how to use locks
    for mutual exclusion """

import threading
import time

x = 8192

lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()

    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached maximum")
    lock.release()


def halve():
    global x, lock
    lock.acquire()

    while x != 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("reached minimum")
    lock.release()


t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)

t1.start()
t2.start()