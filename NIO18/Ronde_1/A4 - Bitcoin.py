bitcoin_value = [int(input()) for _ in range(int(input()))]

s = 0
for i in range(0, len(bitcoin_value) - 1, 1):
    if bitcoin_value[i+1] > bitcoin_value[i]:
        s += bitcoin_value[i+1] - bitcoin_value[i]

print(s)
