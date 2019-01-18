num = int(input())
front = [int(x) for x in input().split()]
right = [int(x) for x in input().split()]


greatest = [front, right][[sum(front), sum(right)].index(max(sum(front), sum(right)))]

N = max(sum(front), sum(right)) + min(greatest)
M = 0

for i in range(num):
    for j in range(num):
        t = min(front[i], right[j])
        M += t

M -= N

print(N, M)
