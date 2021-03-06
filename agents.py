

class GameGraphicsAgent():

    def __init__(self, game):
        self._game = game
        self._info = ""

    def get_title(self):
        return self._game.title

    def get_state(self):
        return self._game.state

    def get_info(self):
        return self._info

    def get_players(self):
        return self._game.players

    def get_turn(self):
        return self._game.turn

    def set_info(self, new_info):
        self._info = new_info
