import operator


class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __len__(self):
        if self.is_empty():
            return 0
        tam = 1
        tam += len(self.left) if self.left else 0
        tam += len(self.right) if self.right else 0
        return tam

    def height(self):
        if self.is_empty():
            return 0
        hl = 1 + self.left.height() if self.left else 0
        hr = 1 + self.right.height() if self.right else 0
        return max(hl, hr)

    def is_empty(self):
        return self.data is None

    def is_elem(self, elem):
        return self.find(elem) is not False

    def __for_all(self, func, br):
        if br is None:
            return True
        else:
            c1 = func(br.data, self.data)
            c2 = c1 and self.__for_all(func, br.left)
            c3 = c2 and self.__for_all(func, br.right)
            return c3

    def is_bst(self):
        if self.is_empty():
            return True
        else:
            c1 = self.__for_all(operator.lt, self.left)
            c2 = c1 and self.__for_all(operator.gt, self.right)
            c3 = c2 and self.left.is_bst() if self.left is not None else True
            c4 = c3 and self.right.is_bst() if self.right is not None else True
            return c4

    def insert(self, data):
        if self.is_empty():
            self.data = data
            return True
        elif self.data == data:
            return False
        elif self.data > data:
            if not self.left is None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if not self.right is None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        if self.is_empty():
            return False
        elif self.data == data:
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
        if self.is_empty():
            return False
        elif self.data == data:
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
                return
            else:
                self.left = self.left.delete(data)
        else:
            if self.right is None:
                return
            else:
                self.right = self.right.delete(data)
        return self

    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()

    def __str__(self):
        text = str(self.left) if self.left is not None else ''
        text += str(self.data) + ' ' if self.data is not None else ''
        text += str(self.right) if self.right is not None else ''
        return text
