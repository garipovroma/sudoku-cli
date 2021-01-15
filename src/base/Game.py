import pickle
import os
from ..error.InvalidMoveError import InvalidMoveError
from ..error.InvalidCommandError import InvalidCommandError
from src.base.Field import Field


class Game:
    commands = ["move", "load", "save", "exit"]

    menu_items = ['new game', 'load game', 'exit']
    int_to_item = {1: 'new game', 2: 'load game', 3: 'exit'}

    def __init__(self, player):
        self.player = player
        self.field = None

    def print_menu(self):
        print("#######Menu##########")
        for i in enumerate(self.menu_items):
            print(str(i[0] + 1) + ") " + i[1])
        print()

    def is_int(self, x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    def run_game(self):
        try:
            os.mkdir("saves")
        except OSError:
            print(">>> Creation of the directory saves failed")
        else:
            print(">>> Successfully created the directory saves")
        while self.field is None:
            self.print_menu()
            item = input().strip()
            item_int = -1
            if self.is_int(item):
                item_int = int(item)
            if not item in self.menu_items and not item_int in self.int_to_item.keys():
                print(">>> Invalid menu item")
            elif item == "new game" or item_int == 1:
                self.field = Field()
            elif item == "load game" or item_int == 2:
                data = None
                print(">>> Enter filename without .pkl")
                filename = input()
                try:
                    with open("saves/" + filename + ".pkl", "rb") as f:
                        data = pickle.load(f)
                except Exception:
                    print(">>> There is no such file or it damaged")
                self.field = Field(data['grid'], data['free_cells'], data['state'], data['last_move'])
            elif item == "exit" or item_int == 3:
                exit(0)

        while self.field.state != "win":
            print(self.field)
            try:
                command = self.player.get_command()
                if command not in self.commands:
                    raise InvalidCommandError("There is no such command")
                elif command == "save":
                    filename = self.player.get_save_filename()
                    data = {'grid': self.field.grid,
                            'free_cells': self.field.free_cells,
                            'state': self.field.state,
                            'last_move': self.field.last_move}
                    with open("saves/" + filename + ".pkl", "wb") as f:
                        pickle.dump(data, f)
                    print(">>> Game saved to saves/" + filename + ".pkl")
                elif command == "move":
                    x, y, value = self.player.get_move()
                    self.field.check_move(x, y, value)
                    self.field.make_move(x, y, value)
                elif command == "exit":
                    exit(0)

            except InvalidMoveError as e:
                self.player.put_error(str(e))
            except InvalidCommandError as e:
                self.player.put_error(str(e))
            except ValueError:
                self.player.put_error("Invalid command format")
        print(">>> You successfully solved sudoku!")
        input()
