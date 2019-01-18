class Board:
    def __init__(self, size):
        self.rows = [['?' for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_row(self, row_id, row):
        self.rows[row_id] = row

    def add_pos(self, pos_x, pos_y, info):
        self.rows[pos_y][pos_x] = info


board = Board(int(input()))
for i in range(board.size):
    board.add_row(i, list(input()))

print(sum([x.count("?") for x in board.rows]))
