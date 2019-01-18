import math


class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def get_name(self):
        return self.name

    def get_edges(self):
        return self.edges

    def add_edge(self, v2, w=None):
        self.edges.append(Edge(self, v2, w))


class Edge:
    def __init__(self, v1, v2, w=None):
        self.v1 = v1
        self.v2 = v2

        if w:
            self.weight = w
        else:
            self.weight = 1

    def get_vertices(self):
        return [self.v1, self.v2]

    def get_weight(self):
        return self.weight


def dijkstra(graph, source, target):
    Q = []
    dist = {}
    prev = {}
    for v in list(graph.keys()):
        dist[v] = 1001
        prev[v] = None
        Q.append(graph[v])

    dist[source] = 0

    while len(Q) > 0:
        t_dist = 1001
        for i in Q:
            if dist[i.get_name()] < t_dist:
                t_dist = dist[i.get_name()]
                u = i

        Q.remove(u)
        if u.get_name() == target:
            break

        for v in [x.v2 for x in u.get_edges()]:
            tmp = [x if x.v2 == v else 0 for x in u.get_edges()]
            for i in range(tmp.count(0)):
                tmp.remove(0)
            alt = dist[u.get_name()] + tmp[0].get_weight()

            if alt < dist[v.get_name()]:
                dist[v.get_name()] = alt
                prev[v.get_name()] = u.get_name()
    S = []
    while prev[target] is not None:
        S.insert(0, target)
        target = prev[target]
    S.insert(0, target)

    return dist, prev


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

d, p = dijkstra(vertices, 0, max(list(vertices.keys())))
print(d[max(list(vertices.keys()))])
