class _Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __len__(self):
        tam = 1
        tam += len(self.left) if self.left is not None else 0
        tam += len(self.right) if self.right is not None else 0
        return tam

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = _Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = _Node(data)
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

    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=' ')

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            return len(self.root)

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if self.is_empty():
            self.root = _Node(data)
        else:
            return self.root.insert(data)

    def find(self, data):
        if self.is_empty():
            return False
        else:
            return self.root.find(data)

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()


