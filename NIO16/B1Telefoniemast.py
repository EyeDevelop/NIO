import math

__author__ = 'eyedevelop'


def pythagoras(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

mens = [[11, 56], [12, 50], [12, 58], [13, 50], [13, 51], [14, 54],
        [14, 57], [15, 57], [17, 57], [17, 58], [19, 51], [19, 58],
        [20, 56], [20, 58], [21, 54], [22, 56], [23, 50], [23, 53],
        [24, 57], [25, 57]]

puntx = 11
punty = 50

pyth_clist = []
finsh = False
next = 0
grid_num = -1
grid_opp = 135
grid_pyth = []

for j in range(135):
    grid_num += 1
    for i in range(len(mens)):
        x = mens[next][0]
        y = mens[next][1]

        if x > puntx:
            a = x - puntx
        else:
            a = puntx - x

        if y > punty:
            b = y - punty
        else:
            b = punty - y

        pyth_clist.append(pythagoras(a, b))
        next += 1
    if puntx != 26:
        puntx += 1
    else:
        puntx = 11
        punty += 1
    next = 0
    grid_pyth.append([[puntx, punty], pyth_clist])
    pyth_clist = []

for v in range(135):
    for m in range(len(grid_pyth)):
        for b in range(len(grid_pyth[m][1])):
            sum += grid_pyth[m][1][b]
