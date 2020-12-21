n = int(input())
w = input()[0]
c = 1
for i in range(n - 1):
    t = input()
    c += t.count(w)

print(c)
