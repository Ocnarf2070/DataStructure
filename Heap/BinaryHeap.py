class BinaryHeap:
    def __init__(self, elem=[]):
        self.heap = []
        for item in elem:
            self.heap.append(item)
            self.__float_up(len(self.heap) - 1)

    def is_empty(self):
        return len(self.heap) == 0

    def __less_than(self, idx1, idx2):
        return self.heap[idx1] < self.heap[idx2]

    def __swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def __float_up(self, idx):
        while idx != 0:
            idxParent = idx // 2
            if self.__less_than(idx, idxParent):
                self.__swap(idx, idxParent)
                idx = idxParent
            else:
                break

    def push(self, elem):
        self.heap.append(elem)
        self.__float_up(len(self.heap) - 1)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def __bubble_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        largest = idx
        if len(self.heap) > left and self.heap[largest] > self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
            largest = right
        if largest != idx:
            self.__swap(idx, largest)
            self.__bubble_down(largest)

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.__swap(0, len(self.heap) - 1)
            _min = self.heap.pop()
            self.__bubble_down(0)
            return _min

    def __str__(self):
        return str(self.heap)
