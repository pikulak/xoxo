from statics import BOARD_SIDE_LENGTH

class WinConditionChecker:

    def __init__(self, board, player_1_win_condition, player_2_win_condition):
        self._board = board
        self._winner = None
        self._player_1_win_condition = player_1_win_condition 
        self._player_2_win_condition = player_2_win_condition
        self.seq = range(1, BOARD_SIDE_LENGTH + 1)

    def win_by_row(self):
        for x in self.seq:
            row = self._board.get_row(x)

            if row == self._player_1_win_condition:
                self._winner = "player_1"
                return True

            if row == self._player_2_win_condition:
                self._winner = "player_2"
                return True

            return False

    def win_by_column(self):
        for y in self.seq:
            col = self._board.get_column(y)

            if col == self._player_1_win_condition:
                self._winner = "player_1"
                return True

            if col == self._player_2_win_condition:
                self._winner = "player_2"
                return True

        return False   

    def win_by_diagonal(self):  
        first_diagonal = self._board.get_first_diagonal()
        second_diagonal = self._board.get_second_diagonal()

        if first_diagonal == self._player_1_win_condition\
        or second_diagonal == self._player_1_win_condition:

            self._winner = "player_1"
            return True

        if first_diagonal == self._player_2_win_condition \
        or second_diagonal == self._player_2_win_condition:

            self._winner = "player_2"
            return True

        return False

    def checkout(self):
        if self.win_by_column() or self.win_by_diagonal() or self.win_by_row():
            return self._winner
        else:
            return False
