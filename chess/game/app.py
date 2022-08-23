from common.board import *

def newGameSetup() -> Board:
  board = Board()
  return board

def run():
  board = newGameSetup()
  board.displayBoard()
  print('')
  board.makeMove(Coord('B7'), Coord('B5'))
  board.makeMove(Coord('B2'), Coord('B4'))
  board.makeMove(Coord('C7'), Coord('C6'))
  board.makeMove(Coord('C2'), Coord('C3'))
  board.makeMove(Coord('A2'), Coord('A3'))
  board.makeMove(Coord('H7'), Coord('H6'))
  board.makeMove(Coord('H2'), Coord('H3'))
  board.makeMove(Coord('G7'), Coord('G1'))
  board.promotePieceAtCoord(Piece.KNIGHT, Coord('G1'))
  board.displayBoard()
  print(Coord('B7'))
  print(' ')
  board.displayBoard(flip=True)