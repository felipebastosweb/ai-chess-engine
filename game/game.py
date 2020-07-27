from .board import *
from .player import *
from .enemy import *

class Game:
    # attributes static
    board = Board()
    players = [Player(), Enemy()]
    # TODO: initialize
    def __init__(self):
        pass
