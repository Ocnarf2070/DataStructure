import random
import unittest

from PriorityQueue import LinkedPriorityQueue as PriorityQueue


# from PriorityQueue import BHPriorityQueue as PriorityQueue


def next_int():
    return random.randint(0, 100)


class AxiomsPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_ax1(self):
        # Queue is empty initially
        self.assertTrue(self.queue.is_empty(), "The queue must be empty")

    def test_ax2(self):
        # If it has a element, it is not empty
        self.queue.enqueue(next_int())
        self.assertFalse(self.queue.is_empty(), "The queue must not be empty")

    def test_ax3(self):
        # When it is inserted a value, the peek will be that value
        value = next_int()
        self.queue.enqueue(value)
        self.assertEqual(self.queue.peek(), value, "The peek element and the inserted value must be equals")

    def test_ax4(self):
        # If it is enqueue a value in a empty queue and the dequeue, the result will be a empty queue
        self.queue.enqueue(next_int())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty(), "After enqueue and dequeue a empty queue, it must be empty as result")

    def test_ax5(self):
        # Enqueue two values in a queue, if in another queue it is enqueue the minimum of the two values, the peek of 
        # both will be equals
        aux = PriorityQueue()
        x, y = next_int(), next_int()
        self.queue.enqueue(x)
        self.queue.enqueue(y)
        aux.enqueue(min(x, y))
        self.assertEqual(self.queue.peek(), aux.peek(), "The peek of both queue must be equals")

    def test_ax6(self):
        # Enqueue two values and then dequeue is equals to first enqueue the minimum value, then dequeue and finally
        # enqueue the maximum value
        aux = PriorityQueue()
        x, y = next_int(), next_int()
        self.queue.enqueue(x)
        self.queue.enqueue(y)
        self.queue.dequeue()
        aux.enqueue(min(x, y))
        aux.dequeue()
        aux.enqueue(max(x, y))
        self.assertEqual(str(self.queue), str(aux))

    def tearDown(self):
        self.queue = None


if __name__ == '__main__':
    unittest.main()
