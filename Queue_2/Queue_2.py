from collections import deque


#
# my_queue = deque()
# my_queue.append(5)
# my_queue.append(10)
# print(my_queue)
# print(my_queue.popleft())


class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def __str__(self):
        return str(self.queue)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if self.size > 0:
            return self.queue[0]
        else:
            return None

    def get_size(self):
        return self.size

# my_queue = Queue()
# my_queue.enqueue(5)
# my_queue.enqueue(10)
# print(my_queue)
# print(my_queue.dequeue())
