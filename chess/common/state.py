from common.enums import *
from common.board import *

class ColorState:
  # TODO Make Player class
  name: str             = None
  color: Color          = None
  kingRookMoved: bool   = False
  queenRookMoved: bool  = False
  kingMoved: bool       = False

  def __init__(self, color, name='Player'):
    self.color = color
    self.name = name

class State:
  def __init__(self, whiteState: ColorState, blackState: ColorState):
    self.colorStates = [whiteState, blackState]
    self.inCheck     = False
    self.turnColor   = Color.WHITE
    # self.lastMove    = Move

  def findCondition(self, board: Board) -> Condition:
    """Finds whether the board state is in check or checkmate, done at the beginning of turn.

    Returns:
        Condition: Returns 
        Condition of boardstate, sets State.incheck to True if Condition is found, or False if not found.
    """
    # find players king (Dict piece tracker?)
    # check if last moved piece causes check
    # check if last moved piece causes disocvered check (did it lie on rank/file/diagonal to king?)
    # if check, check mate (and lose)
    # if neither check nor mate, find at least 1 valid move and return
    # else, stalemate!
    # record state, if same state occurs 3 times then stalemate
    return None
