__author__ = 'eyedevelop'

n = int(input())

begin = "*"*((2*n)-1)
ans = ""
for i in range(n - 1):
    ans += "-" * i + begin[:len(begin) - 2 * i] + "-" * i + "\n"
for i in range(n - 1, -1, -1):
    ans += "-" * i + begin[:len(begin) - 2 * i] + "-" * i + "\n"

print(ans)