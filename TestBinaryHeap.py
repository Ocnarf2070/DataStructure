import Heap as bh

m = bh.BinaryHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
print(m)
print('\n')

ma = bh.MaxHeap([95, 3, 21])
ma.push(10)
print(ma)
print(ma.pop())
print(ma.peek())
print(ma)
