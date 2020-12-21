a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
r = ""
for i in range(int(input())):
    for j in input():
        if j in a:
            a.remove(j)
print(''.join(sorted(a)))
