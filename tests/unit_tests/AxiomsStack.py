import random
import unittest

from Stack import *


def next_int():
    return random.randint(0, 100)


def next_ints():
    return random.sample(range(1, 100), 10)


class AxiomsStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_ax1_1(self):
        # The stack must peek the latest pushed element
        # When the stack is empty
        elem = next_int()
        self.stack.push(elem)
        self.assertEqual(self.stack.peek(), elem, "The peek of the stack must be the latest pushed element")

    def test_ax1_2(self):
        # The stack must peek the latest pushed element
        # When the stack is not empty
        for e in next_ints():
            self.stack.push(e)
        elem = next_int()
        self.stack.push(elem)
        self.assertEqual(self.stack.peek(), elem, "The peek of the stack must be the latest pushed element")

    def test_ax2_1(self):
        # If the stack has pushed and the popped, the stack is the same as the initial after the operations
        # When the stack is empty
        aux = self.stack
        self.stack.push(next_int())
        self.stack.pop()
        self.assertEqual(self.stack, aux, "If a stack is pushed and popped, the new stack must be the same as before")
        # When the stack is not empty

    def test_ax2_2(self):
        # If the stack has pushed and the popped, the stack is the same as the initial after the operations
        # When the stack is not empty
        for e in next_ints():
            self.stack.push(e)
        aux = self.stack
        self.stack.push(next_int())
        self.stack.pop()
        self.assertEqual(self.stack, aux, "If a stack is pushed and popped, the new stack must be the same as before")

    def test_ax3(self):
        # An empty stack is empty
        self.assertTrue(self.stack.is_empty(), "An empty stack must be empty")

    def test_ax4(self):
        # Push return a non-empty stack
        self.stack.push(next_int())
        self.assertFalse(self.stack.is_empty(), "Push must return a non-empty stack")

    def tearDown(self):
        self.stack = None


if __name__ == '__main__':
    unittest.main()
