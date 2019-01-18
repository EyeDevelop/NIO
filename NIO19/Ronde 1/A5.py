import sys
from collections import OrderedDict

n = int(input())
mapper = OrderedDict()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    r = list(input())

    if letters[i] not in mapper.keys():
        mapper[letters[i]] = []

    for l in range(len(r)):
        if r[l] == "1":
            mapper[letters[i]].append(letters[l])


def check_path(point, recursion_depth=0, parents=None):
    ret = []
    if not parents:
        parents = []

    if len(parents) == len(mapper.keys()) - 1:
        print("".join(parents + [point]))
        sys.exit()

    next_points = mapper[point]
    for next_point in next_points:
        path = {}

        if next_point not in parents:
            path[next_point] = check_path(next_point, recursion_depth + 1, parents + [point])

        if len(path.keys()) > 0:
            ret.append(path)

    return ret


for node in mapper.keys():
    check_path(node)
