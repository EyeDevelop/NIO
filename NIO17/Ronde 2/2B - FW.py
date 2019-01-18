import math

class Edge:
    def __init__(self, v1, v2, weight=1):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def get_vertices(self):
        return [self.v1, self.v2]

    def get_weight(self):
        return self.weight


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def get_id(self):
        return self.id

    def add_edge(self, v2, weight):
        edge = Edge(self.get_id(), v2.get_id(), weight)
        self.edges.append(edge)

    def remove_edge(self, v2, weight):
        edge = Edge(self.get_id(), v2.get_id(), weight)
        self.edges.remove(edge)

    def get_edges(self):
        return self.edges


def floyd_warshall(vertices):
    dist = [[1001] * len(vertices) for _ in range(len(vertices))]
    for vertex in vertices.values():
        dist[vertex.get_id() - 1][vertex.get_id() - 1] = 0

        for edge in vertex.get_edges():
            dist[edge.get_vertices()[0] - 1][edge.get_vertices()[1] - 1] = edge.get_weight()

    for k in range(0, len(vertices)):
        for i in range(0, len(vertices)):
            for j in range(0, len(vertices)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


vertices = {}
for l in range(int(input()) - 1):
    v1 = l
    v2 = l + 1

    vertices[v1] = Vertex(v1)
    vertices[v2] = Vertex(v2)

    w = int(input())

    vertices[v1].add_edge(vertices[v2], w)
    vertices[v2].add_edge(vertices[v1], w)

for r in range(len(list(vertices.keys())), len(list(vertices.keys())) + int(input()) - 1):
    v1 = r
    v2 = r + 1

    vertices[v1] = Vertex(v1)
    vertices[v2] = Vertex(v2)

    w = int(input())

    vertices[v1].add_edge(vertices[v2], w)
    vertices[v2].add_edge(vertices[v1], w)

for b in range(int(input())):
    v1, v2, weight = map(int, input().split())
    vertices[v1 - 1].add_edge(vertices[v2 - 1], weight)
    vertices[v2 - 1].add_edge(vertices[v1 - 1], weight)

distances = floyd_warshall(vertices)
print(distances[-1][-2])
