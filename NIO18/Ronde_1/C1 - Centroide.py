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


num = int(input())
vertices = {}
for i in range(1, num + 1):
    vertices[i] = Vertex(i)

for i in range(num - 1):
    v1, v2 = map(int, input().split())
    vertices[v1].add_edge(vertices[v2], 1)

fw = floyd_warshall(vertices)
lengths = {}
for i in range(len(fw)):
    lengths[i + 1] = sum(fw[i])

centres = sorted(lengths.keys(), key=lambda x: lengths[x])
if lengths[centres[0]] == lengths[centres[1]]:
    print(min(centres[0], centres[1]), max(centres[0], centres[1]))
else:
    print(centres[0])
