__author__ = 'eyedevelop'

finished = False
n = []
ans = []
while not finished:
    tmp = int(input())
    if tmp != 0:
        n.append(tmp)
    else:
        finished = True

for i in range(len(n)):
    if (int(n[i]) % 7 == 0) or (list(str(n[i])).__contains__("7")):
        ans.append(i)

print(len(ans))