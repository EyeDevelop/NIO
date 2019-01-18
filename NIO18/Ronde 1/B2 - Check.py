c = 20
n = 1
s = 0
while c > 0:
    a = input("%d: " % n)
    if not a:
        n += 1
        continue
    a = int(a)
    s += n * a
    c -= a
    n += 1

print(s)
