from .piece import *

class Bishop(Piece):
    def move(self):
        if self.is_black:
            pass
        if not self.is_black:
            pass
    # Convert in str
    def __str__():
        return "B" if self.is_black else "b"
