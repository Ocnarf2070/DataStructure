from SearchTree import AVL
from SearchTree import avltree

avl = AVL()
avl2 = avltree()
ls = [1, 6, 3, 5, 8, 4, 2, 8, 3]
for l in ls:
    avl.insert(l)
    print('AVL:' + str(avl))
