import copy


class Tree:
    def __init__(self, data=None, weight=0, left=None, right=None):
        self.data = data
        self.weight = weight
        self.left = left
        self.right = right

    def __len__(self):
        return self.weight

    def is_empty(self):
        return self.data is None

    def is_heap(self):
        if self.is_empty():
            return True
        else:
            left, right = self.left, self.right
            b = self.__less_eq(left) and self.__less_eq(right)
            b = b and left.is_heap() if left is not None else True
            b = b and right.is_heap() if right is not None else True
            return b

    def __less_eq(self, n):
        if n is None:
            return True
        else:
            return self.data <= n.data

    def __merge(self, h2):
        if h2 is None:
            return
        if self.data > h2.data:
            self.data, h2.data = h2.data, self.data
        if self.right is None:
            self.right = h2
        else:
            self.right.__merge(h2)

        w_l = self.left.weight if self.left is not None else 0
        w_r = self.right.weight if self.right is not None else 0
        self.weight = 1 + w_l + w_r
        if w_l < w_r:
            self.left, self.right = self.right, self.left

    def push(self, elem):
        if self.is_empty():
            self.data = elem
        else:
            tree = Tree(elem, 1)
            self.__merge(tree)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data

    def pop(self):
        if self.is_empty():
            return None
        else:
            elem = self.data
            if self.left is not None:
                self.left.__merge(self.right)
                self.data, self.left, self.right = copy.deepcopy((self.left.data, self.left.left, self.left.right))
            else:
                self.__init__()
            return elem

    @staticmethod
    def make_heap(l: list):
        heap = Tree()
        for el in l:
            heap.push(el)
        return heap

    def __str__(self):
        text = str(self.data) + ' ' if self.data is not None else ''
        text += str(self.left) if self.left is not None else ''
        text += str(self.right) if self.right is not None else ''
        return text
