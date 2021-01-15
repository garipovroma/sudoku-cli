from ..error.InvalidMoveError import InvalidMoveError
from ..base import SudokuGridGenerator


class Field:
    def __init__(self, *args):
        self.n = 9
        if len(args) == 0:
            print(">>> Enter filled cells count, integer from [0..80]")
            x = -1
            while x < 0 or x > 80:
                try:
                    x = int(input())
                    if x < 0 or x > 80:
                        print("Invalid value, it should be integer from [0..80]")
                except ValueError:
                    print(">>> Invalid value, it should be integer")
            self.free_cells = 81 - x
            self.grid = SudokuGridGenerator.generate(self.free_cells)
            self.state = "game_running"
            self.last_move = ""
        else:
            self.grid = args[0]
            self.free_cells = args[1]
            self.state = args[2]
            self.last_move = args[3]



    def __str__(self):
        res = "[state : " + self.state + " | free cells : " + str(
            self.free_cells) + " | last_move : " + self.last_move + "]\n"
        for i in range(len(self.grid)):
            if i % 3 == 0:
                res += "\n"
            for j in range(len(self.grid[i])):
                if j % 3 == 0:
                    res += " "
                if self.grid[i][j] != 0:
                    res += str(self.grid[i][j])
                else:
                    res += "_"
                res += " "
            res += "\n"
        return res

    def check_move(self, x, y, value):
        if x < 0 or x > self.n or y < 0 or y > self.n:
            raise InvalidMoveError("cell coordinates should be in [1..9] range")
        if value < 0 or value > 9:
            raise InvalidMoveError("cell value should be in [1..9] range")
        if self.grid[x][y] != 0:
            raise InvalidMoveError("this cell already in use")
        vertical = []
        horizontal = []
        subfield = []
        for i in range(0, self.n):
            cell = self.grid[x][i]
            if cell != -1:
                horizontal.append(cell)
            cell = self.grid[i][y]
            if cell != -1:
                vertical.append(cell)
        subfield_x = x // 3
        subfield_y = y // 3
        for i in range(subfield_x * 3, subfield_x * 3 + 3):
            for j in range(subfield_y * 3, subfield_y * 3 + 3):
                cell = self.grid[i][j]
                if cell != -1:
                    subfield.append(cell)
        if value in vertical or value in horizontal or value in subfield:
            raise InvalidMoveError.InvalidMoveError("you cant place this value here")

    def make_move(self, x, y, value):
        self.grid[x][y] = value
        self.last_move = "[ " + str(x + 1) + " " + str(y + 1) + " " + str(value) + " ]"
        self.free_cells -= 1
        if self.free_cells == 0:
            self.state = "win"
            return True
        return False
