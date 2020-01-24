import operator


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.node = None
        self.height = 0

    def is_empty(self):
        return self.node is None

    def __for_all(self, func, br):
        if br.is_empty():
            return True
        else:
            c1 = func(br.node.data, self.node.data)
            c2 = c1 and self.__for_all(func, br.node.left)
            c3 = c2 and self.__for_all(func, br.node.right)
            return c3

    def is_avl(self):
        if self.is_empty():
            return True
        else:
            c1 = self.__for_all(operator.lt, self.node.left)
            c2 = c1 and self.__for_all(operator.gt, self.node.right)
            c3 = c2 and abs(self.node.left.height - self.node.right.height) <= 1
            c4 = c3 and self.node.left.is_avl()
            c5 = c4 and self.node.right.is_avl()
            return c5

    def right_leaning(self):
        if self.is_empty(): return False
        return self.node.left.height < self.node.right.height

    def left_leaning(self):
        if self.is_empty(): return False
        return self.node.left.height > self.node.right.height

    def update_heights(self, recurse=True):
        if not self.is_empty():
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = 0

    def rot_r(self):
        t = self.node
        lt = self.node.left.node
        rlt = lt.right.node

        self.node = lt
        lt.right.node = t
        t.left.node = rlt

        self.update_heights()

    def rot_l(self):
        t = self.node
        rt = self.node.right.node
        lrt = rt.left.node

        self.node = rt
        rt.left.node = t
        t.right.node = lrt

        self.update_heights()

    def balance(self):
        self.update_heights()
        lh = self.node.left.height
        rh = self.node.right.height

        if lh - rh > 1 and self.node.left.left_leaning():
            self.rot_r()
        elif lh - rh > 1:
            self.node.left.rot_l()
            self.rot_r()
        elif rh - lh > 1 and self.node.right.right_leaning():
            self.rot_l()
        elif rh - lh > 1:
            self.node.right.rot_r()
            self.rot_l()

    def insert(self, elem):
        if self.is_empty():
            self.node = Node(elem)
            self.node.right = Tree()
            self.node.left = Tree()
        elif self.node.data > elem:
            self.node.left.insert(elem)
        elif self.node.data < elem:
            self.node.right.insert(elem)
        self.balance()

    def find(self, elem):
        if self.is_empty():
            return None
        elif self.node.data == elem:
            return self.node.data
        elif self.node.data > elem:
            return self.node.left.find(elem)
        else:
            return self.node.right.find(elem)

    def is_elem(self, elem):
        return self.find(elem) is not None

    def delete(self, elem):
        if not self.is_empty():
            if self.node.data == elem:
                self.node.left.combine(self.node.right)
                self.node = self.node.left.node
            elif self.node.data > elem:
                self.node.left.delete(elem)
                self.balance()
            else:
                self.node.right.delete(elem)
                self.balance()

    def combine(self, right):
        if self.is_empty():
            self.node = right.node
        elif right.is_empty():
            pass
        else:
            left = self.node
            self.node, right = right.split()
            self.node.left.node = left
            self.node.right.node = right.node
            self.balance()

    def split(self):
        if self.node.left.is_empty():
            return self.node, self.node.right
        else:
            root, left = self.node.left.split()
            self.node.left.node = left.node
            self.balance()
            return root, self

    def minim(self):
        if self.is_empty():
            return None
        if self.node.left.is_empty():
            return self.node.data
        else:
            return self.node.left.minim()

    def maxim(self):
        if self.is_empty():
            return None
        if self.node.right.is_empty():
            return self.node.data
        else:
            return self.node.right.minim()

    def __str__(self):
        text = str(self.node.left) if not self.node.left.is_empty() else ''
        text += str(self.node.data) + ' ' if self.node.data is not None else ''
        text += str(self.node.right) if not self.node.right.is_empty() else ''
        return text

    def print_tree_as_tree_shape(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.print_tree_as_tree_shape(node.right.node, level + 1)
            print(('\t' * level), (' / '))
        print(('\t' * level), node.data)

        if node.left.node:
            print(('\t' * level), (' \\ '))
            self.print_tree_as_tree_shape(node.left.node, level + 1)


if __name__ == "__main__":
    avl = Tree()
    print(avl.is_avl())
    ls = [13, 8, 21, 9]
    for l in ls:
        avl.insert(l)
        avl.print_tree_as_tree_shape()
        print(avl.is_avl())
        print('\n')
    print(avl)
    print(avl.minim())
    print(avl.maxim())
    avl.delete(8)
    avl.print_tree_as_tree_shape()
    print(avl.is_avl())
