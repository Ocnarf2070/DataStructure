from Graph import GraphAL, GraphAM

print('Graph Adjacency List')
g = GraphAL()
g.add_vertex('A')
g.add_vertex('B')
for i in range(ord('A'), ord('K')):
    g.add_vertex(chr(i))
print(g)
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[0], edge[1])
print(g)
print('\n')

print('Graph Adjacency Matrix')
g = GraphAM()
g.add_vertex('B')
for i in range(ord('B'), ord('K')):
    g.add_vertex(chr(i))
g.add_vertex('A')
print(g)
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[0], edge[1])
print(g)
