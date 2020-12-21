coins = []
for _ in range(int(input())):
    coins.append(int(input()))
coins = sorted(coins)


def count(m, n):
    t = [[0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(m):
        t[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = t[i - coins[j]][j] if i - coins[j] >= 0 else 0
            y = t[i][j - 1] if j >= 1 else 0

            t[i][j] = x + y

    return t[n][m - 1]


print(count(len(coins), int(input())))
