class _Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = _Node(d, self.root)
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
        prev_node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:  # data is not in the root
                    prev_node.next_node = this_node.next_node
                else:  # data is in the root
                    self.root = this_node.next_node
                this_node = None
                self.size -= 1
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False  # data not found

    def __str__(self):
        aux = ''
        this_node = self.root
        while this_node is not None and this_node.next_node is not None:
            aux += str(this_node) + ' -> '
            this_node = this_node.next_node
        aux += str(this_node)
        return aux

# myList = LinkedList()
# myList.add(5)
# myList.add(3)
# myList.add(8)
# myList.add(12)
# print(myList)
#
# print("size=" + str(myList.size))
# myList.remove(8)
# print("size=" + str(myList.size))
# print(myList.find(5))
# print(myList.root)
# print(myList)
