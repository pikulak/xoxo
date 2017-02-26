import os

from abc import abstractmethod
from statics import PLAYER_1_ID, PLAYER_2_ID

class GraphicsPrototype:
    def __init__(self, middleware):
        self._middleware = middleware
    
    @abstractmethod
    def draw(what):
        raise NotImplementedError

class ConsoleGraphics(GraphicsPrototype):

    def __init__(self, middleware):
        super(ConsoleGraphics, self).__init__(middleware)
        self._title = self._middleware.get_title()
        self._header = self.make_header()

    def make_header(self):
        players = self._middleware.get_players()
        header = ""
        if len(players) > 1:
            player_1 = players[PLAYER_1_ID]
            player_2 = players[PLAYER_2_ID]
            header = "{}({}) | {}({})".format(
                    player_1.name,
                    player_1.marker,
                    player_2.name,
                    player_2.marker)
        return header


    def draw(self):
        os.system("cls")
        draw_ = """
                {title}
                {header}

                -------------
                | {s[1]} | {s[2]} | {s[3]} |
                -------------
                | {s[4]} | {s[5]} | {s[6]} |
                -------------
                | {s[7]} | {s[8]} | {s[9]} |
                -------------
                {info}
                """.format(title=self._title,
                           header=self._header,
                           info=self._middleware.get_info(),
                           s=self._middleware.get_state())
        print(draw_)