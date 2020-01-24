from SearchTree import *

print('BST')
tree = BST(7)
tree.insert(9)
for i in [15, 10, 2, 12, 1, 13, 5, 4, 3, 6, 11, 4, 14, 9]:
    tree.insert(i)
for i in range(16):
    print(tree.find(i), end=' ')
print('\n', len(tree))
tree.preorder()
print()
tree.inorder()
print()
print(tree.minim())
print(tree.height())
print(tree.delete(7))
tree.preorder()
print('\n')
tree.inorder()
print('\n')

print('BSTNode')
tree = BSTNode()
tree.insert(7)
tree.insert(9)
for i in [15, 10, 2, 12, 1, 13, 5, 4, 3, 6, 11, 4, 14, 9]:
    tree.insert(i)
for i in range(16):
    print(tree.find(i), end=' ')
print('\n', len(tree))
tree.preorder()
print()
tree.inorder()
print()
