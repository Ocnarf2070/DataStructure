from List import *

print("LinkedList")
myList = LinkedList()
myList.add(5)
myList.add(3)
myList.add(8)
myList.add(12)
print(myList)

print("size=" + str(myList.size))
myList.remove(8)
print("size=" + str(myList.size))
print(myList.find(5))
print(myList.root)
print(myList)
print('\n')

print("DoubleLinkedList")
dll = DoubleLinkedList()
for i in [5, 9, 3, 8, 9]:
    dll.add(i)

print("size=" + str(dll.size))
print(dll)
dll.remove(8)
print("size=" + str(dll.size))

print(dll.remove(15))
print(dll.find(15))
dll.add(21)
dll.add(22)
dll.remove(5)
print(dll)
print(dll.last.prev_node)
print('\n')

print("CircularLinkedList")
cll = CircularLinkedList()
for i in [5, 7, 3, 8, 9]:
    cll.add(i)

print("size=" + str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print(my_node, end=' -> ')
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end=' -> ')
print()

print(cll)
cll.remove(8)
print(cll.remove(15))
print("size=" + str(cll.size))
cll.remove(5)  # delete root node
print(cll)
