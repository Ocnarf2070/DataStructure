from collections import deque

from Queue_2 import Queue

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())

my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue)
print(my_queue.dequeue())
