from typing import Dict, List, Tuple
from enums import *
from exceptions import *

class Board:
  """Representation of Chess Board and Pieces"""
  # Variables
  __board = [[None for x in range(8)] for y in range(8)]
  __pieceDict = {
    (Color.WHITE, Piece.EMPTY): "\u25FB",
    (Color.WHITE, Piece.PAWN): "\u265F",
    (Color.WHITE, Piece.ROOK): "\u265C",
    (Color.WHITE, Piece.KNIGHT): "\u265E",
    (Color.WHITE, Piece.BISHOP): "\u265D",
    (Color.WHITE, Piece.KING): "\u265A",
    (Color.WHITE, Piece.QUEEN): "\u265B",
    (Color.BLACK, Piece.EMPTY): "\u25FC",
    (Color.BLACK, Piece.PAWN): "\u2659",
    (Color.BLACK, Piece.ROOK): "\u2656",
    (Color.BLACK, Piece.KNIGHT): "\u2658",
    (Color.BLACK, Piece.BISHOP): "\u2657",
    (Color.BLACK, Piece.KING): "\u2654",
    (Color.BLACK, Piece.QUEEN): "\u2655",
  }

  # Constructors
  def __init__(self):
    self.newBoard()

  # Functions  
  def newBoard(self) -> None:
    """Resets board and its pieces to a new game."""
    self.__board[7] = self.__newBackLine(Color.BLACK)
    self.__board[6] = self.__newFrontLine(Color.BLACK)
    for i in range(5, 1, -1):
      self.__board[i] = self.__newEmptyLine() 
    self.__board[1] = self.__newFrontLine(Color.WHITE)
    self.__board[0] = self.__newBackLine(Color.WHITE)
    return None

  def __newBackLine(self, color: Color) -> List[Tuple[Color,Piece]]:
    line = []
    line.append((color, Piece.ROOK))
    line.append((color, Piece.KNIGHT))
    line.append((color, Piece.BISHOP))
    line.append((color, Piece.QUEEN))
    line.append((color, Piece.KING))
    line.append((color, Piece.BISHOP))
    line.append((color, Piece.KNIGHT))
    line.append((color, Piece.ROOK))
    return line

  def __newFrontLine(self, color: Color) -> List[Tuple[Color,Piece]]:
    return [(color, Piece.PAWN) for x in range(8)]

  def __newEmptyLine(self) -> List[None]:
    return [None for x in range(8)]

  def __printLine(self, startingColor: Color, line: List[Tuple[Color, Piece]]) -> None:
    for i in range(8):
      startingColor = (Color) ((startingColor.value + 1) % 2)
      if(line[i] is None):
        print(self.__pieceDict.get((startingColor, Piece.EMPTY))+' ', end='')
      else:
        print(self.__pieceDict.get(line[i])+' ', end='')
    print('')
    return None

  def displayBoard(self, flip:bool = False) -> None:
    """Prints board to console.

    Args:
        flip (bool, optional): When True, board flips to perspective of BLACK. Defaults to False.
    """
    start = 8
    stop = 0
    step = -1

    if flip:
      start = 1
      stop = 9
      step = 1

    for i in range(start,stop,step):
      print(str(i)+' ',end='')
      if(i%2 == 0):
        self.__printLine(Color.WHITE, self.__board[i-1])
      else:
        self.__printLine(Color.BLACK, self.__board[i-1])
    print('  a b c d e f g h')
  
  def getPieceAtCoord(self, coord: Coord) -> Tuple[Color, Piece]:
    """Returns piece at given coordinate.

    Args:
        coord (Coord): Enumerated coordinate.

    Returns:
        Tuple[Color, Piece]: Returns a colored piece.
    """
    rank, file = coord.value
    return self.__board[file][rank]

  def makeMove(self, fromCoord: Coord, toCoord: Coord) -> None:
    """Moves piece 'fromCoord' to 'toCoord'. Does not validate legality.

    Args:
        fromCoord (Coord): Coord of piece's current location
        toCoord (Coord): Coord of piece's future location

    Raises:
        SelectedPieceIsNone: Piece at fromCoord is None

    Returns:
        None
    """
    fromPiece = self.getPieceAtCoord(fromCoord)
    fromRank, fromFile = fromCoord.value
    toRank, toFile = toCoord.value

    if fromPiece[1] == None:          raise SelectedPieceIsNone(fromCoord)
    else:
      self.__board[toFile][toRank] = fromPiece
      self.__board[fromFile][fromRank] = None
    return None

  def promotePieceAtCoord(self, toPiece: Piece, coord: Coord) -> None:
    """Promotes the piece at 'coord' to piece 'toPiece'

    Args:
        toPiece (Piece): Piece the pawn is promoting to
        coord (Coord): Coordinate of piece promoting

    Raises:
        SelectedPieceIsNone: Piece at coord is None
        PromotionToPieceIsInvalid: Piece at toPiece is Piece.PAWN
        PromotionFromPieceIsInvalid: Piece at coord is not Piece.PAWN
        PromotionPieceInvalidRank: coord is not in rank [1,8]

    Returns:
        None
    """
    fromPiece = self.getPieceAtCoord(coord)
    rank, file = coord.value

    if toPiece == None:               raise SelectedPieceIsNone(coord)
    elif toPiece == Piece.PAWN:       raise PromotionToPieceIsInvalid(toPiece)
    elif fromPiece[1] != Piece.PAWN:  raise PromotionFromPieceIsInvalid(fromPiece)
    elif rank != 0 or rank != 7:      raise PromotionPieceInvalidRank(rank)
    else:
      self.__board[file][rank] = (fromPiece[0], toPiece)
    return None
