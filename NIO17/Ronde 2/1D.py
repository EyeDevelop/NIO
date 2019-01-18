c = 0
for i in range(int(input())):
    t = input()
    if len(set(t)) == len(t):
        c += 1

print(c)