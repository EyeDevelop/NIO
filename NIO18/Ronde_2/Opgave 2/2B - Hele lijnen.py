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

amount_of_o_horiz = sum([1 if "0" not in x else 0 for x in board.rows])
amount_of_z_horiz = sum([1 if "1" not in x else 0 for x in board.rows])

vert_board = [["?" for _ in range(board.size)] for _ in range(board.size)]
for i in range(board.size):
    vert_board[i] = [x[i] for x in board.rows]

amount_of_o_vert = sum([1 if "0" not in x else 0 for x in vert_board])
amount_of_z_vert = sum([1 if "1" not in x else 0 for x in vert_board])

print(amount_of_z_horiz + amount_of_z_vert)
print(amount_of_o_horiz + amount_of_o_vert)
