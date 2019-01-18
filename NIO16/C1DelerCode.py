t = list(input())
d = []
for i in range(2, len(t) + 1):
    if len(t) % i == 0:
        d.append(i)

r = []
for i in d:
    r = [t[x:x+i:x] for x in range(1, len(t)-1, i)]

print(r)
