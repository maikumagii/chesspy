from typing import List
from common.enums import *
from common.validate import *

class Move:
  def __init__(self, fromCoord: Coord, toCoord: Coord):
    self.fromCoord = fromCoord
    self.toCoord = toCoord

class StandardAlgebraicNotation:
  validator = Validate()
  condition = Condition.NONE
  move1, move2 = None, None
  san = None

  def __init__(self, unparsedSAN: str):
    self.san = self.__parseSAN(unparsedSAN)

  def __parseSAN(self, unparsedSAN: str):
    self.san = unparsedSAN
    unparsedSAN = self.__checkCheckOrMate(unparsedSAN)
    unparsedSAN = self.__checkPromotion(unparsedSAN)
    if unparsedSAN[-1] == 'O':
      self.__parseCastle(unparsedSAN)
    else:
      self.__parseMove(unparsedSAN)

  def __checkCheckOrMate(self, unparsedSAN: str) -> str:
    if unparsedSAN[-1] == '#':
      if self.validator.validateCheckmate():
        self.condition = Condition.CHECKMATE
      return unparsedSAN[0:len(unparsedSAN)-1]
    elif unparsedSAN[-1] == '+':
      if self.validator.validateCheck():
        self.condition = Condition.CHECK
      return unparsedSAN[:-1]
    else:
      return unparsedSAN
    
  def __checkPromotion(self, unparsedSAN):
    pieces = ['R', 'N', 'B', 'Q']
    if unparsedSAN[-1] in pieces and unparsedSAN == '=':
      self.__parsePromote(unparsedSAN[-1])
    return unparsedSAN[:-2]

  def __parsePromote(self, unparsedSAN):
    pass

  def __parseMove(self, unparsedSAN):
    pass

  def __parseCastle(self, unparsedSAN):
    '''if unparsedSAN == 'O-O-O':
      self.move1 = Move()
    elif unparsedSAN == 'O-O':
    '''
    pass