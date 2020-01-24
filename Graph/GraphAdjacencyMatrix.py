class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, v):
        vertex = Vertex(v)
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def __str__(self):
        txt = ''
        if len(self.vertices) != 0:
            txt += '\t' + '\t'.join(sorted(self.vertices.keys())) + '\n'
            # txt += '\t' + '\t'.join(self.vertices.keys()) + '\n'
        # for v, i in (self.edge_indices.items()):
        for v, i in sorted(self.edge_indices.items()):
            txt += v
            for j in range(len(self.edges)):
                txt += '\t' + str(self.edges[i][j])
            txt += '\n'
        return txt
