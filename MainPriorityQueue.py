import PriorityQueue as PQ

pq = PQ.LinkedPriorityQueue()
persons_priority = [5, 4, 3, 9, 9, 1, 2, 8, 2, 6, 7, 4, 2, 8, 6, 9, 10, 22, 15]
for priority in persons_priority:
    pq.enqueue(priority)
    print(pq)
print(len(pq))
print(pq.peek())
print(pq.dequeue())
print(pq.dequeue())
print(len(pq))
print(pq.peek())

pq = PQ.BHPriorityQueue()
persons_priority = [5, 4, 3, 9, 9, 1, 2, 8, 2, 6, 7, 4, 2, 8, 6, 9, 10, 22, 15]
for priority in persons_priority:
    pq.enqueue(priority)
    print(pq)
print(len(pq))
print(pq.peek())
print(pq.dequeue())
print(pq.dequeue())
print(len(pq))
print(pq.peek())
