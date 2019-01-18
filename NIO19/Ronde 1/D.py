import string


class Player:
    def __init__(self, is_white=False):
        # Player starts as BLACK (ColourID 2; WHITE is 1).
        self.is_white = is_white
        self.__update_colour_id()
        self.pieces_left = 30

    def __update_colour_id(self):
        self.colour_id = (2, 1)[self.is_white]

    def change_colour(self):
        self.is_white = not self.is_white
        self.__update_colour_id()

    def reduce_piece(self, amount=1):
        self.pieces_left -= amount

        if self.pieces_left > 0:
            return True

        return False


class Board:
    def __init__(self, ai_player: Player):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.ai = ai_player
        self.active = False

        self.opponent = Player(not self.ai.is_white)

        self.white_at_turn = True
        self.current_player = None
        self.update_current_player()

        self.move_counter = 0

    @staticmethod
    def __minmax(min_n, max_n, n):
        if n < min_n:
            return min_n
        elif n > max_n:
            return max_n
        else:
            return n

    def print_board(self):
        for row in self.grid:
            print(" | ".join(map(str, row)))

    def handle_input(self, command: str):
        if command == "Start":
            self.ai.change_colour()
            self.opponent.change_colour()

        elif command == "Quit":
            self.stop()

        elif command == "Print":
            self.print_board()

        else:
            self.handle_move(command)

    def start(self):
        self.active = True
        while self.active:
            self.handle_input(input())

    def stop(self):
        self.active = False

    def handle_move(self, move: str):
        if self.current_player.reduce_piece():
            colour = ("Black", "White")[self.current_player.is_white]

            row, column = tuple(move)
            row = string.ascii_uppercase.index(row)
            column = int(column) - 1

            if self.check_move_validity(column, row) or self.move_counter == 0:
                self.grid[row][column] = self.current_player.colour_id
                self.overturn_pieces(column, row, self.current_player.colour_id)

                print("Colour [{}] did move [{}]. Has [{}] pieces left.".format(
                    colour,
                    move,
                    self.current_player.pieces_left
                ))
            else:
                print("Colour [{}] attempted an invalid move!\nExiting.".format(
                    colour
                ))
                self.stop()

        self.move_counter += 1
        self.update_current_player()

    def check_move_validity(self, grid_x, grid_y):
        return (
                self.grid[grid_y][grid_x] == 0 and

                (
                        self.grid[grid_y][self.__minmax(0, 7, self.__minmax(0, 7, grid_x + 1))] != 0 or
                        self.grid[grid_y][self.__minmax(0, 7, self.__minmax(0, 7, grid_x - 1))] != 0 or

                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y + 1))][grid_x] != 0 or
                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y - 1))][grid_x] != 0 or

                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y + 1))][
                            self.__minmax(0, 7, self.__minmax(0, 7, grid_x + 1))] != 0 or
                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y + 1))][
                            self.__minmax(0, 7, self.__minmax(0, 7, grid_x - 1))] != 0 or
                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y - 1))][
                            self.__minmax(0, 7, self.__minmax(0, 7, grid_x + 1))] != 0 or
                        self.grid[self.__minmax(0, 7, self.__minmax(0, 7, grid_y - 1))][
                            self.__minmax(0, 7, self.__minmax(0, 7, grid_x - 1))] != 0
                )
        )

    def overturn_pieces(self, grid_x, grid_y, colour_initiated):
        new_colour = (1, 2)[colour_initiated == 1]

        # region RIGHT
        # Get the last piece
        last_piece_index = 0
        for i in range(self.__minmax(0, 7, grid_x + 1), 8):
            if self.grid[grid_y][i] == 0:
                break

            if self.grid[grid_y][i] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(self.__minmax(0, 7, grid_x + 1), last_piece_index):
            if self.grid[grid_y][i] == colour_initiated:
                self.grid[grid_y][i] = new_colour
            elif self.grid[grid_y][i] == new_colour:
                self.grid[grid_y][i] = colour_initiated
        # endregion

        # region LEFT
        # Get the last piece
        last_piece_index = 0
        for i in range(self.__minmax(0, 7, grid_x - 1), -1, -1):
            if self.grid[grid_y][i] == 0:
                break

            if self.grid[grid_y][i] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(self.__minmax(0, 7, grid_x - 1), last_piece_index, -1):
            if self.grid[grid_y][i] == colour_initiated:
                self.grid[grid_y][i] = new_colour
            elif self.grid[grid_y][i] == new_colour:
                self.grid[grid_y][i] = colour_initiated
        # endregion

        # region BOTTOM
        # Get the last piece
        last_piece_index = 0
        for i in range(self.__minmax(0, 7, grid_y + 1), 8):
            if self.grid[i][grid_x] == 0:
                break

            if self.grid[i][grid_x] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(self.__minmax(0, 7, grid_y + 1), last_piece_index):
            if self.grid[i][grid_x] == colour_initiated:
                self.grid[i][grid_x] = new_colour
            elif self.grid[i][grid_x] == new_colour:
                self.grid[i][grid_x] = colour_initiated
        # endregion

        # region TOP
        # Get the last piece
        last_piece_index = 0
        for i in range(self.__minmax(0, 7, grid_y - 1), -1, -1):
            if self.grid[i][grid_x] == 0:
                break

            if self.grid[i][grid_x] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(self.__minmax(0, 7, grid_y - 1), last_piece_index, -1):
            if self.grid[i][grid_x] == colour_initiated:
                self.grid[i][grid_x] = new_colour
            elif self.grid[i][grid_x] == new_colour:
                self.grid[i][grid_x] = colour_initiated
        # endregion

        # region TOP-RIGHT
        # Get the last piece
        last_piece_index = 0
        for i in range(1, max(grid_x, grid_y) + 1):
            if (
                    self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] == 0 or
                    grid_y - i < 0 or
                    grid_x + i > 7
            ):
                break

            if self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(last_piece_index):
            if self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] == colour_initiated:
                self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] = new_colour
            elif self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] == new_colour:
                self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x + i)] = colour_initiated
        # endregion

        # region TOP-LEFT
        # Get the last piece
        last_piece_index = 0
        for i in range(1, max(grid_x, grid_y) + 1):
            if (
                    self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] == 0 or
                    grid_y - i < 0 or
                    grid_x - i < 0
            ):
                break

            if self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(last_piece_index):
            if self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] == colour_initiated:
                self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] = new_colour
            elif self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] == new_colour:
                self.grid[self.__minmax(0, 7, grid_y - i)][self.__minmax(0, 7, grid_x - i)] = colour_initiated
        # endregion

        # region BOTTOM-LEFT
        # Get the last piece
        last_piece_index = 0
        for i in range(min(grid_x, grid_y)):
            if (
                    self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] == 0 or
                    grid_y + i > 7 or
                    grid_x - i < 0
            ):
                break

            if self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(last_piece_index):
            if self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] == colour_initiated:
                self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] = new_colour
            elif self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] == new_colour:
                self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x - i)] = colour_initiated
        # endregion

        # region BOTTOM-RIGHT
        # Get the last piece
        last_piece_index = 0
        for i in range(max(grid_x, grid_y)):
            if (
                    self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] == 0 or
                    grid_y + i > 7 or
                    grid_x + i > 7
            ):
                break

            if self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] == colour_initiated:
                last_piece_index = i

        # Update pieces
        for i in range(last_piece_index):
            if self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] == colour_initiated:
                self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] = new_colour
            elif self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] == new_colour:
                self.grid[self.__minmax(0, 7, grid_y + i)][self.__minmax(0, 7, grid_x + i)] = colour_initiated
        # endregion

    def update_current_player(self):
        if self.ai.is_white == self.white_at_turn:
            self.current_player = self.ai
        else:
            self.current_player = self.opponent

        self.white_at_turn = not self.white_at_turn


def main():
    ai = Player()

    board = Board(ai)
    board.print_board()
    board.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
