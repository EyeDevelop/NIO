import string


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


vertices = {}
for i in range(1, 16 + 1):
    vertices[i] = Vertex(i)

v_weight = [
    ['A', 'B', '12'],
    ['A', 'E', '17'],
    ['A', 'F', '28'],
    ['B', 'C', '19'],
    ['B', 'F', '26'],
    ['C', 'D', '6'],
    ['C', 'F', '31'],
    ['C', 'G', '15'],
    ['C', 'H', '36'],
    ['D', 'H', '17'],
    ['E', 'F', '3'],
    ['E', 'I', '17'],
    ['E', 'J', '30'],
    ['F', 'G', '21'],
    ['F', 'J', '3'],
    ['G', 'H', '16'],
    ['G', 'J', '34'],
    ['G', 'K', '25'],
    ['G', 'L', '26'],
    ['H', 'L', '16'],
    ['I', 'J', '28'],
    ['I', 'M', '20'],
    ['I', 'N', '27'],
    ['J', 'K', '13'],
    ['J', 'N', '28'],
    ['K', 'L', '27'],
    ['K', 'N', '39'],
    ['K', 'O', '23'],
    ['K', 'P', '29'],
    ['L', 'P', '7'],
    ['M', 'N', '5'],
    ['N', 'O', '19'],
    ['O', 'P', '16']
]

for i in range(len(v_weight)):
    v1, v2, weight = v_weight[i]
    v1 = string.ascii_uppercase.index(v1) + 1
    v2 = string.ascii_uppercase.index(v2) + 1
    weight = int(weight)
    vertices[v1].add_edge(vertices[v2], weight)

fw = floyd_warshall(vertices)
ind = fw[0].index(max(fw[0]))
print("Longest way from A is to %s, it takes %d minutes." % (str(string.ascii_uppercase[ind]), fw[0][ind]))
