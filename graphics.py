import os
import _thread
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

from flask import Flask, render_template
from abc import abstractmethod
from statics import PLAYER_1_ID, PLAYER_2_ID
from prototypes import GraphicsPrototype


class WebGraphics(GraphicsPrototype):
    def __init__(self, middleware):
        super(WebGraphics, self).__init__(middleware)
        self._title = self._middleware.get_title()
        self._header = ""

    def init(self):
        self._header = self.make_header()
        _thread.start_new_thread(self.flask_app, (None,))

    def make_header(self):
        players = self._middleware.get_players()
        header = ""
        if len(players) > 1:
            player_1 = players[PLAYER_1_ID]
            player_2 = players[PLAYER_2_ID]
            header = "{}({}) | WEB HEADER | {}({})".format(
                    player_1.name,
                    player_1.marker,
                    player_2.name,
                    player_2.marker)
        return header

    def draw(self):
        pass

    def flask_app(self, _):
        app = Flask(__name__)
        app.secret_key = "some_secret"

        @app.route('/')
        def main():
            state = self._middleware.get_state()
            info = self._middleware.get_info()
            return render_template('main.html',
                         title=self._title,
                         header=self._header,
                         state=state,
                         info=info)
        app.run()


class ConsoleGraphics(GraphicsPrototype):

    def __init__(self, middleware):
        super(ConsoleGraphics, self).__init__(middleware)
        self._title = self._middleware.get_title()
        self._header = ""


    def init(self):
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