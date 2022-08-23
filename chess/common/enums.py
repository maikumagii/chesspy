from enum import *
from typing import Tuple

class Color(Enum):
  WHITE = 0
  BLACK = 1

class Condition(Enum):
  CHECK = auto()
  CHECKMATE = auto()

class Piece(Enum):
  EMPTY = auto()
  PAWN = auto()
  ROOK = auto()
  KNIGHT = auto()
  BISHOP = auto()
  KING = auto()
  QUEEN = auto()

class Coord:
  file, rank, value = (0, 0, 0)

  def __init__(self, pos: str) -> None:
    self.__posToCoord(pos)

  def __posToCoord(self, pos: str) -> None:
    self.file = ord((str(pos)[0]).upper()) - ord('A')
    self.rank = int(str(pos)[1]) - 1
    self.value = (self.rank, self.file)
  
  def getFile(self) -> int:
    return self.file
  
  def getRank(self) -> int:
    return self.rank

  def getValue(self) -> Tuple[int, int]:
    return self.value