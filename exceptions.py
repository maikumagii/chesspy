from enums import *

class PromotionFromPieceIsInvalid(Exception):
  def __init__(self, piece: Piece, message="Cannot promote a non-pawn piece") -> None:
    self.piece = piece
    self.message = message
    super().__init__(self.message)
  
  def __str__(self):
    return f'{self.piece} -> {self.message}'

class PromotionToPieceIsInvalid(Exception):
  def __init__(self, piece: Piece, message="Cannot promote to a pawn piece") -> None:
    self.piece = piece
    self.message = message
    super().__init__(self.message)
  
  def __str__(self):
    return f'{self.piece} -> {self.message}'


class SelectedPieceIsNone(Exception):
  def __init__(self, coord: Coord, message="Selected coordinate is empty") -> None:
    self.coord = coord
    self.message = message
    super().__init__(self.message)
  
  def __str__(self):
    return f'{self.coord} -> {self.message}'

class PromotionPieceInvalidRank(Exception):
  def __init__(self, rank: int, message="Can only promote on ranks 1 and 9") -> None:
    self.rank = rank + 1
    self.message = message
    super().__init__(self.message)
  
  def __str__(self):
    return f'{self.rank} -> {self.message}'

class PieceDoesNotExist(Exception):
  pass