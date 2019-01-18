class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, v2, weight=1):
        self.edges[v2.get_name()] = weight
        v2.__add_edge(self, weight)

    def __add_edge(self, v2, weight=1):
        self.edges[v2.get_name()] = weight

    def get_edges(self):
        return self.edges

    def get_name(self):
        return self.name


def dijkstra(vertices, source):
    Q = []
    dist = {}
    prev = {}

    for v in vertices.keys():
        dist[v] = float('inf')
        prev[v] = None
        Q.append(v)

    dist[source] = 0

    dist2 = dict(dist)
    while len(Q) > 0:
        u = vertices[min(dist2.keys(), key=dist.get)]
        Q.remove(u.get_name())
        dist2.pop(u.get_name())

        for n in u.get_edges().keys():
            alt = dist[u.get_name()] + u.get_edges()[n]
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u.get_name()

    return dist, prev


def floyd_warshall(vertices):
    dist = [[float('inf')] * max(vertices.keys()) for _ in range(max(vertices.keys()))]
    for v in vertices.keys():
        dist[v - 1][v - 1] = 0

        for e in vertices[v].get_edges().keys():
            dist[e - 1][v - 1] = vertices[v].get_edges()[e]

    for k in range(len(vertices.keys())):
        for i in range(len(vertices.keys())):
            for j in range(len(vertices.keys())):
                if dist[i - 1][j - 1] > dist[i - 1][k - 1] + dist[k - 1][j - 1]:
                    dist[i - 1][j - 1] = dist[i - 1][k - 1] + dist[k - 1][j - 1]

    return dist


vertices = {}
print("Please enter the amount of nodes.")
for i in range(1, int(input()) + 1):
    vertices[i] = Vertex(i)

print("Now, please enter the edges between the nodes.")
print("Format: Node1 (to) Node2 (with weight) Weight")
print("End with a # on an empty line.")
while True:
    t = input()
    if t == "#":
        break
    v1, v2, weight = map(int, t.split())
    vertices[v1].add_edge(vertices[v2], weight)

# IMPLEMENTATION DIJKSTRA

print("Please enter the nodes to go from A to B.")
print("Format: A B")
f, t = map(int, input().split())
d1, p = dijkstra(vertices, f)
r = []
i = t

print(p)

if d1[t] != float('inf'):
    while i != f:
        r += ["%s -> %s" % (p[i], i)]
        i = p[i]

    print('\n'.join(r[::-1]))
    print("Shortest distance: %d" % d1[t])
else:
    print("%d can never reach %d!" % (f, t))


# IMPLEMENTATION FLOYD-WARSHALL

# distances = floyd_warshall(vertices)
# center = []
# max_dist = None
# for i in distances:
#     tmp = max(i)
#     if not max_dist:
#         max_dist = tmp
#
#     if tmp < max_dist:
#         max_dist = tmp
#         center.clear()
#         center.append(distances.index(i) + 1)
#     elif tmp == max_dist:
#         center.append(distances.index(i) + 1)
#
# print(*center)
