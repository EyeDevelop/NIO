__author__ = 'eyedevelop'

inv = []
for i in range(10):
    inv.append(input())


def getValueAtXY(x, y):

    xd = {k: 0 for k in range(10)}
    for xn in range(len(inv[0])):
        xd.__setitem__(xn, list(str(inv[int(y)]))[xn])

    yd = {k: 0 for k in range(10)}
    for yn in range(len(inv[0])):
        yd.__setitem__(yn, list(str(inv[yn]))[int(x)])

    return xd[x]

finished = False
name = 1
huidig_x = 0
huidig_y = 0
gebieden = []
y_checked = []
k = 0

while not finished:
    if (huidig_y == 9) and (huidig_x == 9):
        finished = True
    else:
        if getValueAtXY(huidig_x, huidig_y) == '0':
            max_x = 8 - huidig_x
            if y_checked == huidig_x:
                continue
            else:
                while getValueAtXY(huidig_x + k, huidig_y) != '1':
                    gebieden.append([name, [[huidig_x,huidig_y]]])
                    y_checked.append(huidig_y)
                    if k == max_x:
                        break
                    else:
                        k += 1
            if huidig_x == 9:
                huidig_x = 0
                huidig_y += 1
            else:
                huidig_x += 1
        else:
            if huidig_x == 9:
                huidig_x = 0
                huidig_y += 1
            else:
                huidig_x += 1

print(gebieden)