from game import app

if __name__ == '__main__':
  app.run()





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