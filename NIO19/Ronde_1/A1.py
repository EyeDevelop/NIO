n = int(input())
m = int(input())
v = int(input())

start = "*" * n
for i in range(m):
    print(start)
    start += "*" * v
