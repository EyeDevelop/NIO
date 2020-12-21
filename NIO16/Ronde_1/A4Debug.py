__author__ = 'eyedevelop'

n = int(input())
w = []
for i in range(n):
    w.append(int(input()))

n_next = 9
start = 0
ans = []

for j in range(n):

    if n_next == n:
        break

    f10 = w[start:n_next]
    f10_s = sorted(f10)

    highest = f10_s[len(f10_s) - 1:]

    ans.append(highest)
    print(f10)
    print(f10_s)
    print(highest)

    delrange = 0
    for k in range(len(f10)):
        if f10[k] == highest[0]:
            print(str(f10[k]))
            delrange = k

    start += delrange + 1
    n_next = start + 10

f10 = w[start:n_next]
f10_s = sorted(f10)

highest = f10_s[len(f10_s) - 1:]

ans.append(highest)
print(f10)
print(f10_s)
print(highest)

delrange = 0
for k in range(len(f10)):
    if f10[k] == highest[0]:
        print(str(f10[k]))
        delrange = k

print(ans)
