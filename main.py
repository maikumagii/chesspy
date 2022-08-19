from enums import *
from board import *
from game import *

# TODO Make unit tests to test validity of board.py
#      - Setup / New Board
#      - Move Piece
#      - Promotion
#      - Board flip
# TODO Create game logic into game.py
#      - Interpret input as chess move
#        - Resolve ambiguity
#      - Validate move as legal
#        - Can Piece move to Square if nothing is in the way?
#        - Is something in the way?
#        - Does moving piece put piece owner's king in check?
#        - Castling
#          - Tracking movement of king and rook
#        - En Passant
#          - Tracking opponents last move
#      - End of move checks
#        - Promotion
#        - Check
#          - Discovered Check
#        - Checkmate
# TODO Game flow ?
# TODO Player database ?
# TODO Networking ?

board = newGameSetup()
board.displayBoard()
print('')
board.makeMove(Coord.B7, Coord.B5)
board.makeMove(Coord.B2, Coord.B4)
board.makeMove(Coord.C7, Coord.C6)
board.makeMove(Coord.C2, Coord.C3)
board.makeMove(Coord.A2, Coord.A3)
board.makeMove(Coord.H7, Coord.H6)
board.makeMove(Coord.H2, Coord.H3)
board.displayBoard()
print(' ')
board.displayBoard(flip=True)