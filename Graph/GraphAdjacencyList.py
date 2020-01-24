class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        vertex = Vertex(v)
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def __str__(self):
        txt = ''
        for key in sorted(list(self.vertices.keys())):
            txt += str(key) + ' -> ' + str(sorted(list(self.vertices[key].neighbors))) + '\n'
        return txt
