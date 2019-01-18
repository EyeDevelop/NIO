s = d = 0
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(int(input())):
    t = input()
    if "".join(sorted(t)) == t:
        s += 1
    if "".join(sorted(t, reverse=True)) == t:
        d += 1

print(s, d)
