from typing import List
from common.enums import *
from common.validate import *

class Move:
  def __init__(self, piece: Piece, fromCoord: Coord, toCoord: Coord):
    self.piece = piece
    self.fromCoord = fromCoord
    self.toCoord = toCoord

class StandardAlgebraicNotation:
  def __init__(self, unparsedSAN: str):
    self.san = self.__parseSAN(unparsedSAN)

  def __parseSAN(self, unparsedSAN: str):
    pieces = ['R', 'N', 'B', 'K', 'Q']
    rank = [str(x+1) for x in range(0,8)]
    file = [chr(x+ord('a')) for x in range(0,8)]
    validator = Validate()

    if unparsedSAN[-1] in pieces:
      self.__parsePromote()
    elif unparsedSAN[-1] in pieces:
      self.__parseMove()
    elif unparsedSAN[-1] == '+':
      validator.validateCheck()
      self.__parseSAN(unparsedSAN[:-1])
    elif unparsedSAN[-1] == '#':
      validator.validateCheckmate()
      self.__parseSAN(unparsedSAN[:-1])
    elif unparsedSAN[-1] == 'O':
      self.__parseCastle()

  def __parsePromote(self):
    pass

  def __parseMove(self):
    pass

  def __parseCastle(self):
    pass