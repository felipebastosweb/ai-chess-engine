import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros(64).reshape(8, 8)
    # TODO: Verify if is game over
    def is_game_over(self):
        pass
    # TODO: Verify if is c
    def is_check(self):
        pass
    # TODO: Verify if is checkmate
    def checkmate(self):
        pass
    # TODO: convert 
    def __str__(self):
        pass

