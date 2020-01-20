class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = []
        for item in items:
            self.heap.append(item)
            self.__float_up(self.size() - 1)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.heap.append(data)
        self.__float_up(self.size() - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None

    def pop(self):
        if self.size() > 2:
            self.__swap(1, self.size() - 1)
            max = self.heap.pop()
            self.__bubble_down(1)
        elif self.size() == 2:
            max = self.heap.pop()
        else:
            max = None
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if self.size() > left and self.heap[largest] < self.heap[left]:
            largest = left
        if self.size() > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def __str__(self):
        return str(self.heap)


m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
