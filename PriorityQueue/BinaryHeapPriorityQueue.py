import copy

import Heap.BinaryHeap as bh


class BHPriorityQueue:
    def __init__(self):
        self.heap = bh()

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return self.heap.is_empty()

    def enqueue(self, elem):
        self.heap.push(elem)

    def peek(self):
        return self.heap.peek()

    def dequeue(self):
        return self.heap.pop()

    def __str__(self):
        aux = copy.deepcopy(self)
        text = 'LinkedPriorityQueue ('
        while not aux.is_empty():
            elem = aux.heap.pop()
            text += str(elem) + ' -> '
        text = text[0:-4]
        text += ')'
        return text
