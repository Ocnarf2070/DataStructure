import copy
import random
import unittest

from SearchTree import AVL


def next_int():
    return random.randint(0, 100)


def next_ints():
    return random.sample(range(1, 100), 10)


class AxiomsBST(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()

    def test_ax1(self):
        # An empty AVL is a AVL
        self.assertTrue(self.avl.is_avl())

    def test_ax2(self):
        # Inserting a element in a AVL is still a AVL
        for el in next_ints():
            self.avl.insert(el)
        self.avl.insert(next_int())
        self.assertTrue(self.avl.is_avl())

    def test_ax3(self):
        # Deleting a element in a AVL is still a AVL
        for el in next_ints():
            self.avl.insert(el)
        self.avl.delete(next_int())
        self.assertTrue(self.avl.is_avl())

    def test_ax4(self):
        # A empty AVL is empty
        self.assertTrue(self.avl.is_empty(), "A empty AVL must be empty")

    def test_ax5(self):
        # Inserting a element in an empty AVL it results a non-empty AVL
        self.avl.insert(next_int())
        self.assertFalse(self.avl.is_empty(), "Inserting a element in an empty AVL must result in a non-empty BST")

    def test_ax6(self):
        # Searching a element in a empty AVL will return that there is not element in that AVL
        self.assertFalse(self.avl.is_elem(next_int()), "Searching in a empty AVL must return False")

    def test_ax7_1(self):
        # Two elements are the same if it is inserted one in the AVL and it found the other
        # or the other element is already in the original AVL.
        # When it is an empty BST
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.avl)
        self.avl.insert(x)
        self.assertTrue(self.avl.is_elem(x_p) == (x_p == x) or t.is_elem(x_p))

    def test_ax7_2(self):
        # Two elements are the same if it is inserted one in the AVL and it found the other
        # or the other element is already in the original AVL.
        # When it is a non-empty BST
        for el in next_ints():
            self.avl.insert(el)
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.avl)
        self.avl.insert(x)
        self.assertTrue(self.avl.is_elem(x_p) == (x_p == x) or t.is_elem(x_p))

    def test_ax8_1(self):
        # If it is inserted an element in a AVL, finding it will return the element
        # When it is an empty AVL
        x = next_int()
        self.avl.insert(x)
        self.assertTrue(self.avl.find(x) == x, "Inserting a element and finding it must return the same element")

    def test_ax8_2(self):
        # Two elements are the same if it is inserted one in the BST and it found the other
        # or the other element is already in the original BST.
        # When it is a non-empty BST
        for el in next_ints():
            self.avl.insert(el)
        x = next_int()
        self.avl.insert(x)
        self.assertTrue(self.avl.find(x) == x, "Inserting a element and finding it must return the same element")

    def test_ax9_1(self):
        # If it is inserted one element in the BST and it found in another element, these two element are equals
        # or the other element is already in the original BST.
        # When it is an empty BST
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.avl)
        self.avl.insert(x)
        self.assertTrue((self.avl.find(x_p) == x) == (x_p == x or t.find(x_p) == x))

    def test_ax9_2(self):
        # If it is inserted one element in the BST and it found in another element, these two element are equals
        # or the other element is already in the original BST.
        # When it is a non-empty BST
        for el in next_ints():
            self.avl.insert(el)
        x = next_int()
        x_p = next_int()
        t = copy.deepcopy(self.avl)
        self.avl.insert(x)
        self.assertTrue((self.avl.find(x_p) == x) == (x_p == x or t.find(x_p) == x))

    def test_ax10_1(self):
        # If it is deleted a element from a BST, that element cannot be found later.
        # When it is an empty BST
        x = next_int()
        self.avl.delete(x)
        self.assertFalse(self.avl.is_elem(x), "Deleting a element and then find it must return False")

    def test_ax10_2(self):
        # If it is deleted a element from a BST, that element cannot be found later.
        # When it is a non-empty BST
        for el in next_ints():
            self.avl.insert(el)
        x = next_int()
        self.avl.delete(x)
        self.assertFalse(self.avl.is_elem(x), "Deleting a element and then find it must return False")

    def tearDown(self):
        self.avl = None


if __name__ == '__main__':
    unittest.main()
