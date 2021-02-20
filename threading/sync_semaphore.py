import threading
import time

sem = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print(f"{thread_number} is trying to access")
    sem.acquire()

    print(f"{thread_number} granted access")
    time.sleep(10)

    print(f"{thread_number} is now releasing!")
    sem.release()


for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
