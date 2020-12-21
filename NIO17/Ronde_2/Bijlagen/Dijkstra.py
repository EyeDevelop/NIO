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
        dist[v] = math.inf
        prev[v] = None
        Q.append(graph[v])

    dist[source] = 0

    while len(Q) > 0:
        t_dist = math.inf
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


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

v1.add_edge(v2, 9)
v2.add_edge(v1, 9)

v2.add_edge(v3, 16)
v3.add_edge(v2, 16)

v4.add_edge(v5, 4)
v5.add_edge(v4, 4)

v5.add_edge(v6, 5)
v6.add_edge(v5, 5)

v6.add_edge(v7, 20)
v7.add_edge(v6, 20)

v2.add_edge(v4, 2)
v4.add_edge(v2, 2)

v3.add_edge(v7, 30)
v7.add_edge(v3, 30)


graph = {
    1: v1,
    2: v2,
    3: v3,
    4: v4,
    5: v5,
    6: v6,
    7: v7
}

d, p = dijkstra(graph, 1, 3)
print(d)
print(p)
