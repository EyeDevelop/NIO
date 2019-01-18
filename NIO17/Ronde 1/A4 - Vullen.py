field = [[int(j) for j in input()] for i in range(10)]
area = [[0 for x in range(len(field[0]))] for y in range(len(field))]


def increment(item, max):
    if item + 1 <= max:
        item += 1
    else:
        item = 1

    return item


def unwrap_array(array):
    new_array = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            new_array += [array[i][j]]

    return new_array


def update_field():
    global area
    global field
    for y in range(len(area)):
        for x in range(len(area[0])):
            if area[y][x] != 0:
                field[y][x] = increment(field[y][x], 6)


def check_node(x, y):
    global area

    req = field[0][0]

    area[0][0] = req

    if 0 <= x < len(field[y]) - 1:
        if field[y][x + 1] == req and area[y][x + 1] != req:
            area[y][x + 1] = req
            check_node(x + 1, y)

    if 0 < x <= len(field[y]):
        if field[y][x - 1] == req and area[y][x - 1] != req:
            area[y][x - 1] = req
            check_node(x - 1, y)

    if 0 <= y < len(field) - 1:
        if field[y + 1][x] == req and 0 <= y < len(field) - 1 and area[y + 1][x] != req:
            area[y + 1][x] = req
            check_node(x, y + 1)

    if 0 < y <= len(field):
        if field[y - 1][x] == req and area[y - 1][x] != req:
            area[y - 1][x] = req
            check_node(x, y - 1)


count = 0
while True:
    for i in range(0, 10):
        if not check_node(0, i):
            break
    update_field()
    count += 1

    if len(set(unwrap_array(area))) == 1:
        break

print(count)
