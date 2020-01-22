from Heap import *

print("BinaryHeap")
m = BinaryHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
print(m)
print('\n')

print("MaxHeap")
ma = MaxHeap([95, 3, 21])
ma.push(10)
print(ma)
print(ma.pop())
print(ma.peek())
print(ma)
print('\n')

print("WBLHeap")
wblh = WBLHeap()
for elem in [95, 3, 21]:
    wblh.push(elem)
wblh.push(10)
print(wblh)
print(wblh.pop())
print(wblh.peek())
print(wblh)
while not wblh.is_empty():
    print('Pop:' + str(wblh.pop()))
    print(wblh)
