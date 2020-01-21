# Stack using Python list
# my_stack = list()
# my_stack.append(2)
# my_stack.append(7)
# my_stack.append(13)
# my_stack.append(3)
# print(my_stack)
# print(my_stack.pop())
# print(my_stack)


# class
class Stack:
    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def size(self):
        return len(self)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[self.size() - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

