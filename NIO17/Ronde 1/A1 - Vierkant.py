sq = int(input())
for i in range(sq):
    if i == 0 or i == sq - 1:
        print("*" * sq)
        continue
    print("*" + "-"*(sq-2) + "*")