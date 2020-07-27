
class Piece:
    def __init__(self, pos_x, pos_y, color = True):
      self.x = pos_x
      self.y = pos_y
      self.is_black = color ? 1 : 0

