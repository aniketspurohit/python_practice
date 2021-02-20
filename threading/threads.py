import threading


def func1():
    for i in range(1000):
        print("Hello World")


def func2():
    for i in range(1000):
        print("Aniket")


""" Threads allow the users to run multiple functions at the same time! """
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)

# t1.start()
# t2.start()

""" join() doesn't allow the main thread to execute unless the current thread finishes execution"""
t1 = threading.Thread(target=func1)  # Referring func without calling it
t1.start()
t1.join()

print("Hey there")