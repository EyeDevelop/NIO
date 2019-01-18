field = [[int(x) for x in list(input())] for _ in range(10)]
area = [[0] * 10 for _ in range(10)]
area[0][0] = 1


def unwrap_array(arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_arr.append(arr[i][j])

    return new_arr


def update_field(new_color):
    global field
    global area

    for y in range(len(area)):
        for x in range(len(area[y])):
            if area[y][x] != 0:
                field[y][x] = new_color


def check_node(x, y, req):
    global field
    global area

    area[0][0] = req

    if 0 <= x < len(area[y]) - 1:
        if field[y][x + 1] == req and area[y][x + 1] != req:
            area[y][x + 1] = req
            check_node(x + 1, y, req)

    if 0 < x <= len(area[y]):
        if field[y][x - 1] == req and area[y][x - 1] != req:
            area[y][x - 1] = req
            check_node(x - 1, y, req)

    if 0 <= y < len(area) - 1:
        if field[y + 1][x] == req and area[y + 1][x] != req:
            area[y + 1][x] = req
            check_node(x, y + 1, req)

    if 0 < y <= len(area):
        if field[y - 1][x] == req and area[y - 1][x] != req:
            area[y - 1][x] = req
            check_node(x, y - 1, req)


count = 0
while len(set(unwrap_array(field))) > 1:
    orig = field[0][0]
    check_node(0, 0, orig)

    x, y = 0, 0
    while field[y][x] == orig:
        if x + 1 < len(field[y]):
            x += 1
        else:
            if y + 1 < len(field):
                x = 0
                y += 1
            else:
                break

    req = field[y][x]

    update_field(req)

    count += 1

print(count)
