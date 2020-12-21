N, M = map(int, input().split())

left = list(input())
right = list(input())
time = int(input())

new_len = len(left) + len(right)
indexes_r = dict(zip(left, range(len(left) - 1, -1, -1)))
indexes_b = dict(zip(right, range(len(left), new_len)))

for i in range(time):
    to_update_r = {}
    to_update_b = {}
    for red in indexes_r:
        ind = {}
        for blue in indexes_b:
            ind[indexes_b[blue] - indexes_r[red]] = blue
        if 1 in ind.keys():
            to_update_r[red] = 1
            to_update_b[ind[1]] = -1

    for red in to_update_r:
        indexes_r[red] += to_update_r[red]
    for blue in to_update_b:
        indexes_b[blue] += to_update_b[blue]


new_str = [" "] * new_len
for red in indexes_r:
    new_str[indexes_r[red]] = red
for blue in indexes_b:
    new_str[indexes_b[blue]] = blue

print("".join(new_str))
