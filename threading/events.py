import threading
import time

event = threading.Event()


def myfunc():
    """ The event waits for the trigger using wait(). 
    The moment it gets triggered using set(), it prints the line following wait """

    print("Waiting for func to get triggered...\n")
    event.wait()
    print("Performing the event...\n")


t1 = threading.Thread(target=myfunc)
t1.start()

x = input("Do you want to trigger the event? (y/n)?")
if x == "y":
    event.set()
