from typing import List, Tuple
from common.enums import *
from common.exceptions import *

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
    rank, file = coord.getValue()
    return self.__board[rank][file]

  def setPieceAtCoord(self, coord: Coord, piece: Tuple[Color, Piece]) -> None:
    """Returns piece at given coordinate.

    Args:
        coord (Coord): Enumerated coordinate.
        pice (Tuple[Color, Piece]): Colored piece to set.

    Returns:
        None
    """
    rank, file = coord.getValue()
    self.__board[rank][file] = piece
    return None

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

    if fromPiece[1] == None:          raise SelectedPieceIsNone(fromCoord)
    else:
      self.setPieceAtCoord(fromCoord, None)
      self.setPieceAtCoord(toCoord, fromPiece)
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

    print(coord.getRank())
    if toPiece == None: raise SelectedPieceIsNone(coord)
    elif toPiece == Piece.PAWN: raise PromotionToPieceIsInvalid(toPiece)
    elif fromPiece[1] != Piece.PAWN: raise PromotionFromPieceIsInvalid(fromPiece)
    elif coord.getRank() != 0 and coord.getRank() != 7: raise PromotionPieceInvalidRank(coord.getRank())
    else:
      self.setPieceAtCoord(coord, (fromPiece[0], toPiece))
    return None
