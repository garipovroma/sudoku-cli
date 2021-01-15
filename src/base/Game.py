from ..error.InvalidMoveError import InvalidMoveError


class Game:
    def __init__(self, player):
        self.player = player
        self.field = None

    def run_game(self, field):
        self.field = field
        while self.field.state != "win":
            print(self.field)
            try:
                x, y, value = self.player.get_move()
                self.field.check_move(x, y, value)
                self.field.make_move(x, y, value)
            except InvalidMoveError as e:
                self.player.put_move_error(str(e))
        print(">>> You successfully solved sudoku!")
        input()
