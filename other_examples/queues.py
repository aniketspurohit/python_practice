import queue

q1 = queue.Queue()
q2 = queue.LifoQueue()
q3 = queue.PriorityQueue()

nums = [1, 2, 3, 4, 5]

for i in nums:
    q1.put(i)
    q2.put(i)
    q3.put((i, i * 3))

print(q1.get())  # Prints 1 (FIFO)
print(q2.get())  # Prints 5 (LIFO)
print(q3.get())  # Prints (1, 3) Lower value gets higher priority
