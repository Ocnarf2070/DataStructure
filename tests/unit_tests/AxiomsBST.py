import copy
import random
import unittest

from SearchTree import BST


# The next import have some missing methods. Do not try use it.
# from SearchTree import BSTNode as BST


def next_int():
    return random.randint(0, 100)


def next_ints():
    return random.sample(range(1, 100), 10)


class AxiomsPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_ax1(self):
        # An empty BST is a BST
        self.assertTrue(self.bst.is_bst())

    def test_ax2(self):
        # Inserting a element in a BST is still a BST
        for el in next_ints():
            self.bst.insert(el)
        self.bst.insert(next_int())
        self.assertTrue(self.bst.is_bst())

    def test_ax3(self):
        # Deleting a element in a BST is still a BST
        for el in next_ints():
            self.bst.insert(el)
        self.bst.delete(next_int())
        self.assertTrue(self.bst.is_bst())

    def test_ax4(self):
        # A empty BTS is empty
        self.assertTrue(self.bst.is_empty(), "A empty BST must be empty")

    def test_ax5(self):
        # Inserting a element in an empty BTS it results a non-empty BTS
        self.bst.insert(next_int())
        self.assertFalse(self.bst.is_empty(), "Inserting a element in an empty BST must result in a non-empty BST")

    def test_ax6(self):
        # Searching a element in a empty BST will return that there is not element in that BST
        self.assertFalse(self.bst.is_elem(next_int()), "Searching in a empty BST must return False")

    def test_ax7_1(self):
        # Two elements are the same if it is inserted one in the BST and it found the other
        # or the other element is already in the original BST.
        # When it is an empty BST
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.bst)
        self.bst.insert(x)
        self.assertTrue(self.bst.is_elem(x_p) == (x_p == x) or t.is_elem(x_p))

    def test_ax7_2(self):
        # Two elements are the same if it is inserted one in the BST and it found the other
        # or the other element is already in the original BST.
        # When it is a non-empty BST
        for el in next_ints():
            self.bst.insert(el)
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.bst)
        self.bst.insert(x)
        self.assertTrue(self.bst.is_elem(x_p) == (x_p == x) or t.is_elem(x_p))

    def test_ax8_1(self):
        # If it is inserted an element in a BST, finding it will return the element
        # When it is an empty BST
        x = next_int()
        self.bst.insert(x)
        self.assertTrue(self.bst.find(x) == x, "Inserting a element and finding it must return the same element")

    def test_ax8_2(self):
        # Two elements are the same if it is inserted one in the BST and it found the other
        # or the other element is already in the original BST.
        # When it is a non-empty BST
        for el in next_ints():
            self.bst.insert(el)
        x = next_int()
        self.bst.insert(x)
        self.assertTrue(self.bst.find(x) == x, "Inserting a element and finding it must return the same element")

    def test_ax9_1(self):
        # If it is inserted one element in the BST and it found in another element, these two element are equals
        # or the other element is already in the original BST.
        # When it is an empty BST
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.bst)
        self.bst.insert(x)
        self.assertTrue((self.bst.find(x_p) == x) == (x_p == x or t.find(x_p) == x))

    def test_ax9_2(self):
        # If it is inserted one element in the BST and it found in another element, these two element are equals
        # or the other element is already in the original BST.
        # When it is a non-empty BST
        for el in next_ints():
            self.bst.insert(el)
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.bst)
        self.bst.insert(x)
        self.assertTrue((self.bst.find(x_p) == x) == (x_p == x or t.find(x_p) == x))

    def test_ax10_1(self):
        # If it is deleted a element from a BST, that element cannot be found later.
        # When it is an empty BST
        x = next_int()
        self.bst.delete(x)
        self.assertFalse(self.bst.is_elem(x), "Deleting a element and the find it must return False")

    def test_ax10_2(self):
        # If it is deleted a element from a BST, that element cannot be found later.
        # When it is a non-empty BST
        for el in next_ints():
            self.bst.insert(el)
        x = next_int()
        self.bst.delete(x)
        self.assertFalse(self.bst.is_elem(x), "Deleting a element and the find it must return False")

    def tearDown(self):
        self.bst = None


if __name__ == '__main__':
    unittest.main()
