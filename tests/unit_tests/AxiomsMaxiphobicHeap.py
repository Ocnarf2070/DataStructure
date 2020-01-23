import copy
import random
import unittest

from Heap import BinaryHeap as Heap


# from Heap import WBLHeap as Heap


def next_int(mini=0, maxi=100):
    return random.randint(mini, maxi)


def next_ints():
    return random.sample(range(1, 100), 10)


def to_list(heap: Heap):
    l = []
    while not heap.is_empty():
        l.append(heap.pop())
    return l


def is_sorted(l: list):
    i = 0
    while i < len(l) - 1 and l[i] < l[i + 1]:
        i += 1
    return i == len(l) - 1


def same_elements(l1: list, l2: list):
    return set(l1) == set(l2)


class AxiomsMaxiphobicHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_ax1(self):
        # A empty heap is a heap
        self.assertTrue(self.heap.is_heap(), "A empty heap must be a heap")

    def test_ax2_1(self):
        # Inserting a elem in a heap makes the heap not empty
        # When the heap is empty
        self.heap.push(next_int())
        self.assertFalse(self.heap.is_empty(), "Pushing a element must result in a non-empty heap")

    def test_ax2_1(self):
        # Pushing a elem in a heap makes the heap not empty
        # When the heap is not empty
        for el in next_ints():
            self.heap.push(el)
        self.heap.push(next_int())
        self.assertFalse(self.heap.is_empty(), "Pushing a element must result in a non-empty heap")

    def test_ax3_1(self):
        # Pushing a elem in a heap the result it is a heap
        # When the heap is empty
        self.heap.push(next_int())
        self.assertTrue(self.heap.is_heap(), "Pushing a element in a heap must result in another heap")

    def test_ax3_2(self):
        # Pushing a elem in a heap the result it is a heap
        # When the heap is empty
        for el in next_ints():
            self.heap.push(el)
        self.heap.push(next_int())
        self.assertTrue(self.heap.is_heap(), "Pushing a element in a heap must result in another heap")

    def test_ax4(self):
        # Pushing a element in a empty heap, the peek is that element
        elem = next_int()
        self.heap.push(elem)
        self.assertEqual(self.heap.peek(), elem, "The pushed element and the peek of the heap must be equals")

    def test_ax5(self):
        # Pushing a element which is greater than the peek of an non-empty heap, the peek will be the same
        for el in next_ints():
            self.heap.push(el)
        elem = self.heap.peek()
        self.heap.push(next_int(mini=elem))
        self.assertEqual(self.heap.peek(), elem, "The peek element must not change when it is pushed a greater element")

    def test_ax6(self):
        # Pushing a element in an empty heap and popping that heap the result will be an empty heap
        self.heap.push(next_int())
        self.heap.pop()
        self.assertTrue(self.heap.is_empty(), "Pushing and popping in an empty heap must result in another empty heap")

    def test_ax7(self):
        # Popping in a non-empty heap, the new heap is a heap
        for el in next_ints():
            self.heap.push(el)
        self.heap.pop()
        self.assertTrue(self.heap.is_heap(), "Popping a non-empty heap must generate a heap")

    def test_ax8(self):
        # If it is popped a non-empty heap, the new peek will be greater or equals than the popped element
        for el in next_ints():
            self.heap.push(el)
        elem = self.heap.pop()
        self.assertLessEqual(elem, self.heap.peek(), "The popped element must be lesser of equals than the new peek")

    def test_ax9(self):
        # If a list is converted to a heap, when we converted the heap to a list, this would be sorted and will be the
        # same elements as before the conversions
        x = list(next_ints())
        h = Heap.make_heap(x)
        y = to_list(h)
        self.assertTrue(is_sorted(y) and same_elements(x, y), "The list converted to a heap and the to a list must be "
                                                              "sorted and must have the same elements to the original")

    def test_ax10_1(self):
        # Pushing x and then y to a heap is similar to pushing y and the x in the same heap.
        # When the heap is empty
        x, y = next_int(), next_int()
        heap_aux = copy.deepcopy(self.heap)
        self.heap.push(x)
        self.heap.push(y)
        heap_aux.push(y)
        heap_aux.push(x)
        self.assertTrue(same_elements(to_list(self.heap), to_list(heap_aux)))

    def test_ax10_2(self):
        # Pushing x and then y to a heap is similar to pushing y and the x in the same heap.
        # When the heap is not empty
        for el in next_ints():
            self.heap.push(el)
        x, y = next_int(), next_int()
        heap_aux = copy.deepcopy(self.heap)
        self.heap.push(x)
        self.heap.push(y)
        heap_aux.push(y)
        heap_aux.push(x)
        self.assertTrue(same_elements(to_list(self.heap), to_list(heap_aux)))

    def tearDown(self):
        self.queue = None


if __name__ == '__main__':
    unittest.main()
