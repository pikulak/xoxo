from abc import abstractmethod

from inputs import LocalPlayerInput


class PlayerPrototype():

    def __init__(self, marker, name):
        self._marker = marker
        self._name = name
        self._input = LocalPlayerInput

    @property
    def marker(self):
        return self._marker

    @property
    def name(self):
        return self._name

    @abstractmethod
    def move(self):
        raise NotImplementedError


class ArtificialPlayerPrototype(PlayerPrototype):

    def __init__(self, marker, game):
        PlayerPrototype.__init__(self, marker, "AI")
        self._game = game


class GraphicsPrototype:

    def __init__(self, game_graphics_agent):
        self._game_graphics_agent = game_graphics_agent
    
    @abstractmethod
    def init(self):
        raise NotImplementedError

    @abstractmethod
    def draw(what):
        raise NotImplementedError