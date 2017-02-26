import random

from prototypes import PlayerPrototype
from prototypes import ArtificialPlayerPrototype

class HumanPlayer(PlayerPrototype):

    def move(self):
        return self._input.get_next_move(self)

class ArtificialPlayer(ArtificialPlayerPrototype):

    def move(self):
        available_moves = self._game.board.get_available_moves()
        selected_move = random.choice(available_moves)
        return selected_move
