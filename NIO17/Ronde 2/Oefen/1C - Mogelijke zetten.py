class Node:

    global field

    def __init__(self, c, r):
        self.c = c
        self.r = r

    def get_row(self):
        return self.r

    def get_column(self):
        return self.c


a = "abcdefghijklmnopqrstuvwxyz"
mc, mr = list(input())
field = {}

for i in range(a.index(mc)+1): field[a[i]] = []

for i in range(int(input())):
    if i % 2 == 0:
        tmp = list(input())
        field[tmp[0]] += [int(tmp[1]), int(tmp[2])]
    else:
        tmp = list(input())
        field[tmp[0]] += [int(tmp[2])]
        field[tmp[1]] += [int(tmp[2])]

print(field)
