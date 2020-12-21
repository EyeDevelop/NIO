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

    def add_edge(self, v2):
        edge = Edge(self.get_id(), v2.get_id())
        self.edges.append(edge)

    def remove_edge(self, v2):
        edge = Edge(self.get_id(), v2.get_id())
        self.edges.remove(edge)

    def get_edges(self):
        return self.edges


def floyd_warshall(vertices):
    dist = [[1000] * len(vertices) for _ in range(len(vertices))]
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
for _ in range(int(input()) - 1):
    v1, v2 = [int(x) for x in input().split()]
    if v1 not in vertices.keys():
        vertex = Vertex(v1)
        vertices[vertex.get_id()] = vertex

    if v2 not in vertices.keys():
        vertex = Vertex(v2)
        vertices[vertex.get_id()] = vertex

    vertices[v1].add_edge(vertices[v2])
    vertices[v2].add_edge(vertices[v1])

distances = floyd_warshall(vertices)
max_dist = None
center = []

for i in distances:
    tmp = max([x for x in i])

    if not max_dist:
        max_dist = tmp

    if tmp < max_dist:
        max_dist = tmp
        center.clear()
        center.append(distances.index(i) + 1)
    elif tmp == max_dist:
        center.append(distances.index(i) + 1)

print(*sorted(center))
