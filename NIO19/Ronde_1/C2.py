import copy


class Board:
    def __init__(self, grid, printing_allowed=True):
        self.grid = grid
        self.player_location = self.get_player_location()
        self.running = False
        self.score = 0
        self.printing_allowed = printing_allowed
        self.moves_without_diamond = 0
        self.moves = 0

        # region typedef

        self.DIAMOND = 0
        self.WALL = 1
        self.BOMB = 2
        self.STOP = 3
        self.EMPTY = 4

        # endregion

        # region directiondef

        self.U = 0
        self.D = 4
        self.L = 6
        self.R = 2

        self.UR = 1
        self.DR = 3

        self.UL = 7
        self.DL = 5

        # endregion

    def print_board(self):
        temp_grid = copy.deepcopy(self.grid)  # Make a copy of grid, not a reference.
        temp_grid[self.player_location[1]][self.player_location[0]] = "&"
        for row in temp_grid:
            self.print(" | ".join([str(x) for x in row]))
            
    def print(self, *args, **kwargs):
        if self.printing_allowed:
            print(*args, **kwargs)

    def get_player_location(self):
        for row in range(len(self.grid)):
            for item in range(len(self.grid[row])):
                if self.grid[row][item] == "@":
                    return item, row

        return None

    def get_type(self, pos_x, pos_y):
        type_object = self.grid[pos_y][pos_x]
        if type_object == "+":
            return self.DIAMOND
        elif type_object == "#":
            return self.WALL
        elif type_object == "*":
            return self.BOMB
        elif type_object == "O":
            return self.STOP
        elif type_object == "-":
            return self.EMPTY

    def handle_move(self, direction):
        # Y -= 1 is up.
        # X -= 1 is left.
        direction_map = {
            self.U: (0, -1),
            self.UR: (1, -1),
            self.R: (1, 0),
            self.DR: (1, 1),
            self.D: (0, 1),
            self.DL: (-1, 1),
            self.L: (-1, 0),
            self.UL: (-1, -1)
        }
        direction = direction_map[direction]

        self.moves += 1
        self.moves_without_diamond += 1
        if self.moves_without_diamond >= 20:
            self.print("Moved too much without getting a diamond.")
            exit(0)

        done_moving = False
        hit_edge = False
        old_x = self.player_location[0]
        old_y = self.player_location[1]
        while not done_moving:
            new_x = self.player_location[0] + direction[0]
            new_y = self.player_location[1] + direction[1]

            if not (0 <= new_x <= 7) or not (0 <= new_y <= 9):
                hit_edge = True
                done_moving = True

            if hit_edge:
                new_x = old_x
                new_y = old_y

            self.player_location = (new_x, new_y)

            if self.get_type(self.player_location[0], self.player_location[1]) == self.DIAMOND:
                self.moves_without_diamond = 0
                self.score += 1
                self.grid[self.player_location[1]][self.player_location[0]] = " "

            if self.get_type(self.player_location[0], self.player_location[1]) == self.STOP:
                done_moving = True

            if self.get_type(self.player_location[0], self.player_location[1]) == self.WALL:
                done_moving = True
                self.player_location = (old_x, old_y)

            if self.get_type(self.player_location[0], self.player_location[1]) == self.BOMB:
                self.print("!! Hit a bomb. Score: 0 !!")
                exit(0)

            old_x = new_x
            old_y = new_y

    def start_human(self):
        self.running = True
        self.printing_allowed = True
        self.print_board()

        while self.running:
            if self.score >= 16:
                self.print("Maximum score achieved:", self.score)
                self.print("Amount of moves:", self.moves)
                exit(0)

            command = input("> ")
            if command.lower() == "exit" or command.lower() == "q":
                self.running = False
                self.print("Your score:", self.score)
                self.print("Amount of moves:", self.moves)

            elif command.lower() == "print":
                self.print_board()

            elif command.lower() == "score":
                self.print("Your score:", self.score)
                self.print("Amount of moves:", self.moves)

            else:
                directions = map(int, list(command))
                for direction in directions:
                    self.handle_move(direction)

                self.print_board()


if __name__ == '__main__':
    # grid = [list(input()) for _ in range(10)]
    grid = "-*O++-#-\n*-#-#+*O\n-O#O**-*\n*+O-##*+\n*+**O+--\nO++#+*--\nO++#*#*O\n+#O+O#-+\n#@OO#O#-\nOO#+*-*#"
    grid = [list(x) for x in grid.split("\n")]

    b = Board(grid)

    try:
        b.start_human()
    except KeyboardInterrupt:
        exit(0)
