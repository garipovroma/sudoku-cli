from src.base.Game import Game
from src.base import Field
from src.player import HumanPlayer

game = Game(HumanPlayer.HumanPlayer())
game.run_game(Field.Field())
