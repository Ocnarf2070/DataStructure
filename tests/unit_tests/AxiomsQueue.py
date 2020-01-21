import random
import unittest

from Queue_2 import *


def next_int():
    return random.randint(0, 100)


class AxiomsQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_ax1(self):
        # The peek of a empty queue enqueued with a value it is that value
        value = next_int()
        self.queue.enqueue(value)
        self.assertEqual(self.queue.peek(), value, "The enqueued element and the peek of the queue must be equals")

    def test_ax2(self):
        # If the queue is not empty and it is enqueued with a value, the peek will not be that value
        self.queue.enqueue(next_int())
        aux = self.queue
        self.queue.enqueue(next_int())
        self.assertEqual(self.queue.peek(), aux.peek(), "The peek after and before the introduction must be the same "
                                                        "element")

    def test_ax3(self):
        # If the queue is not empty and it is enqueued and then dequeue, it is the same as first dequeue that queue
        # and then enqueue
        self.queue.enqueue(next_int())
        aux = self.queue
        elem = next_int()
        self.queue.enqueue(elem)
        self.queue.dequeue()
        aux.dequeue()
        aux.enqueue(elem)
        self.assertEqual(self.queue, aux, "Enqueue and dequeue an non-empty queue it must be the same as"
                                          "dequeue and enqueue the same queue ")

    def test_ax4(self):
        # If it is enqueue a value in a empty queue and the dequeue, the result will be a empty queue
        self.queue.enqueue(next_int())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty(), "After enqueue and dequeue a empty queue, it must be empty as result")

    def test_ax5(self):
        # Queue is empty initially
        self.assertTrue(self.queue.is_empty(), "The queue must be empty")

    def test_ax6(self):
        # If it has a element, it is not empty
        self.queue.enqueue(next_int())
        self.assertFalse(self.queue.is_empty(), "The queue must not be empty")

    def tearDown(self):
        self.queue = None


if __name__ == '__main__':
    unittest.main()
