class HumanPlayer:
    def get_move(self):
        print(">>> Enter [x] [y] [value]")
        move_string = input()  # x y value
        x, y, value = map(int, move_string.split())
        return x - 1, y - 1, value

    def put_move_error(self, error_msg):
        print(">>>", error_msg, sep=" ")
