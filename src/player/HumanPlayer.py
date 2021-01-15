class HumanPlayer:
    def get_command(self):
        print(">>> Enter command : ['move', 'save', 'exit']")
        command = input().strip()
        return command

    def get_move(self):
        print(">>> Enter [x] [y] [value]")
        move = input()
        x, y, value = map(int, move.split())
        return x - 1, y - 1, value

    def get_save_filename(self):
        print(">>> Enter filename")
        filename = input()
        return filename

    def put_error(self, error_msg):
        print(">>>", error_msg, sep=" ")
