class _Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class DoubleLinkedList:

    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def is_empty(self):
        return self.root is None

    def add(self, d):
        if self.is_empty():
            self.root = _Node(d)
            self.last = self.root
        else:
            new_node = _Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return False

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:  # delete a middle node
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:  # delete last node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:  # delete root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                this_node = None
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def __str__(self):
        aux = ''
        this_node = self.root
        while this_node is not None and this_node.next_node is not None:
            aux += str(this_node) + ' -> '
            this_node = this_node.next_node
        aux += str(this_node)
        return aux

# dll = DoubleLinkedList()
# for i in [5, 9, 3, 8, 9]:
#     dll.add(i)
#
# print("size=" + str(dll.size))
# print(dll)
# dll.remove(8)
# print("size=" + str(dll.size))
#
# print(dll.remove(15))
# print(dll.find(15))
# dll.add(21)
# dll.add(22)
# dll.remove(5)
# print(dll)
# print(dll.last.prev_node)
