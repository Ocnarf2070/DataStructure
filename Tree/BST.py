class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def minim(self):
        if self.left is None:
            return self.data
        else:
            return self.left.minim()

    def maxim(self):
        if self.right is None:
            return self.data
        else:
            return self.right.minim()

    def delete(self, data):
        if self.data == data:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                temp = self.right.minim()
                self.delete(temp)
                self.data = temp
        elif self.data > data:
            if self.left is None:
                return False
            else:
                self.left = self.left.delete(data)
        else:
            if self.right is None:
                return False
            else:
                self.right = self.right.delete(data)
        return self

    def __len__(self):
        if self.left is not None and self.right is not None:
            return 1 + len(self.left) + len(self.right)
        elif self.left:
            return 1 + len(self.left)
        elif self.right:
            return 1 + len(self.right)
        else:
            return 1

    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()


tree = Tree(7)
tree.insert(9)
for i in [15, 10, 2, 12, 1, 13, 5, 4, 3, 6, 11, 4, 14, 9]:
    tree.insert(i)
for i in range(16):
    print(tree.find(i), end=' ')
print('\n', len(tree))
tree.preorder()
print()
tree.inorder()
print()
print(tree.minim())
print(tree.delete(3))
tree.preorder()
