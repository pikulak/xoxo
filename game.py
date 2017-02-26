#!C:/Python34/python.exe
import random
import os

from players import HumanPlayer, ArtificialPlayer
from graphics import ConsoleGraphics, WebGraphics
from middlewares import GameGraphicsMiddleware
from statics import PLAYER_1_ID, PLAYER_2_ID, MOVE_FAILED_FEEDBACK
from checkers import WinConditionChecker
from prototypes import GraphicsPrototype

class Board:

    def __init__(self):
        self._state = {x: x for x in range(1,10)}

    @property
    def state(self):
        return self._state.copy()

    def get_row(self, row_no):
        start = 1 + (3 * (row_no -1))
        end = start + 3
        row = [self._state[i] for i in range(start, end)]
        return row

    def get_column(self, column_no):
        start = column_no
        end = start + 7
        step = 3
        column = [self._state[i] for i in range(start, end, step)]
        return column

    def get_first_diagonal(self):
        return [self._state[i] for i in range(1, 10, 4)]

    def get_second_diagonal(self):
        return [self._state[i] for i in range(3, 8, 2)]

    def get_available_moves(self):
        available_moves = []
        for position, marker in self._state.items():
            if marker not in ["X", "O"]:
                available_moves.append(position)
        return available_moves

    def is_move_possible(self, move):
        if move in self.get_available_moves():
            return True
        else:
            return False

    def put(self, what, where):
        if self.is_move_possible(where):
            self._state[where] = what
            return True
        else:
            return False

    def clear(self):
        self._state = {x:"#" for x in range(1, 10)}


class Game:
    
    def __init__(self):
        self._winner = None
        self._turn = PLAYER_1_ID
        self._players = []
        self._board = Board()
        self._title = "Kolko i krzyzyk"
        self._middleware = GameGraphicsMiddleware(self)
        self._graphics = WebGraphics(self._middleware)

    @property
    def winner(self):
        return self._winner

    @property
    def turn(self):
        return self._turn

    @property
    def board(self):
        return self._board

    @property
    def players(self):
        return self._players[:]

    @property
    def state(self):
        return self._board.state

    @property
    def title(self):
        return self._title

    @property
    def graphics(self):
        return self._graphics

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @graphics.setter
    def graphics(self, new_graphics):
        if isistance(new_graphics, GraphicsPrototype):
            self._graphics = new_graphics
        else:
            raise ValueError("Specifed graphics doesn't implement GraphicalInterface class")

    def init_graphics(self):
        self._graphics.init()

    def get_player(self, which):
        return self._players[which]

    def add_player(self, player):
        if len(self._players) < 2:
            self._players.append(player)

    def make_move(self, where):
        player = self.get_player(self._turn)
        return self._board.put(what=player.marker, where=where)

    def tick(self):
        info = ""
        current_turn = self._turn
        current_player = self.get_player(current_turn) # Player's object

        while True:
            next_move = current_player.move()
            if next_move and self.make_move(next_move):
                self._turn = not self._turn

                info = "{} moved successfully!".format(current_player.name)
                self._middleware.set_info(info)
                self._graphics.draw()
                break
            else:
                self._middleware.set_info(MOVE_FAILED_FEEDBACK)
                self._graphics.draw()

    def check_win(self):
        player_1 = self.get_player(PLAYER_1_ID)
        player_2 = self.get_player(PLAYER_2_ID)

        player_1_win_condition = [player_1.marker] * 3
        player_2_win_condition = [player_2.marker] * 3
        condition_checkout = WinConditionChecker(
                                      self._board,
                                      player_1_win_condition,
                                      player_2_win_condition).checkout()

        if condition_checkout == "player_1":
            self._winner = player_1
            return True

        elif condition_checkout == "player_2":
            self._winner = player_2
            return True

        return False

    def start(self):

        player_1_marker = input("Choose mark for first player: ")
        game_with_ai = input("Do you want play with ai? (y/n): ")
        if player_1_marker == "X":

            if game_with_ai == "y":
                player_1 = HumanPlayer("X", "Player 1")
                player_2 = ArtificialPlayer("O", self)
            else:
                player_1 = HumanPlayer("X", "Player 1")
                player_2 = HumanPlayer("O", "Player 2")
        else:

            if game_with_ai == "y":
                player_1 = ArtificialPlayer("X", self)
                player_2 = HumanPlayer("O", "Human player")
            else:
                player_1 = HumanPlayer("O", "Player 1")
                player_2 = HumanPlayer("X", "Player 2")

        self.add_player(player_1)
        self.add_player(player_2)
        
        self._board.clear()
        self._graphics.init()
        self._graphics.draw()

    def end(self):
        if self._winner is None:
            print("Dead-heat!")
        else:
            print(self._winner.name, "won a game!")

    def run(self):
        self.start()
        while self.check_win() is not True and len(self._board.get_available_moves()) > 0:
            self.tick()
        self.end()


if __name__ == "__main__":
    game = Game()
    game.run()