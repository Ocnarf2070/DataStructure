class _Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedPriorityQueue:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.root is None

    def enqueue(self, elem):
        if self.is_empty():
            self.root = _Node(elem)
        else:
            new_node = _Node(elem)
            prev, curr = None, self.root
            while curr is not None and curr.data < elem:
                prev = curr
                curr = curr.next
            if prev is None:
                new_node.next = self.root
                self.root = new_node
            else:
                new_node.next = curr
                prev.next = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            elem = self.root.data
            self.root = self.root.next
            self.size -= 1
            return elem

    def peek(self):
        return self.root.data

    def __str__(self):
        text = 'LinkedPriorityQueue ('
        this_node = self.root
        while this_node is not None and this_node.next is not None:
            text += str(this_node) + ' -> '
            this_node = this_node.next
        text += str(this_node) + ')'
        return text
