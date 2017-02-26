from abc import abstractmethod


class InputInterface:

    @abstractmethod
    def get_next_move():
        raise NotImplementedError


class LocalPlayerInput(InputInterface):

    def get_next_move(player):
        prompt = "{}'s ({}) turn: ".format(player.name, player.marker)

        try:
            next_move = int(input(prompt))
            return next_move
        except ValueError:
            return False