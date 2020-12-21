class Board:
    def __init__(self, size):
        self.rows = [['?' for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_row(self, row_id, row):
        self.rows[row_id] = row

    def add_pos(self, pos_x, pos_y, info):
        self.rows[pos_y][pos_x] = info

    def get_info(self, pos_x, pos_y):
        return self.rows[pos_y][pos_x]


board = Board(int(input()))
for i in range(board.size):
    board.add_row(i, list(input()))


def get_size(start_x, start_y):
    max_x = None
    max_y = None

    try:
        max_x = board.rows[start_y].index("1", start_x)
    except ValueError:
        max_x = 7

    for i in range(start_y, board.size):
        try:
            if board.rows[i].index("1", start_x) < max_x:
                max_y = i
                break
        except ValueError:
            continue

    if not max_y:
        max_y = 7

    size = (max_x - start_x) * (max_y - start_y)
    return size


sizes = []
for y in range(board.size):
    for x in range(board.size):
        sizes.append(get_size(x, y))

print(max(sizes))
