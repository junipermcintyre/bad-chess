from .piece import Piece
from .pawn import Pawn
from .castle import Castle
from .knight import Knight
from .bishop import Bishop
from .queen import Queen
from .king import King

# Chess class!
class Chess:
    """A chess class, for running chess games"""
    spaces =[[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

    whiteKing = None
    blackKing = None

    """Build the chess board"""
    def __init__(self):
        self.resetBoard()

    """Display board"""
    def printBoard(self):
        boardStr = "    A   B   C   D   E   F   G   H\n"
        boardStr += "  +---+---+---+---+---+---+---+---+\n"
        for i in range(0,8):
            boardStr += str(i) + " | ";
            for j in range(0,8):
                coord = {'x':j, 'y':i}
                piece = self.getPiece(coord)
                if piece != None:
                    boardStr += piece.getSymbol() + " | "
                else:
                    boardStr += "  | "
            boardStr += str(i) + "\n"
            boardStr += "  +---+---+---+---+---+---+---+---+\n"

        boardStr += "    A   B   C   D   E   F   G   H\n"
        return boardStr

    """Display legend"""
    def printLegend(self):
        legendStr = "CHESS BOARD LEGEND\n"
        pawn = Pawn("white")
        castle = Castle("white")
        bishop = Bishop("white")
        knight = Knight("white")
        queen = Queen("white")
        king = King("white")
        legendStr += pawn.getSymbol() + ":    Pawn\n"
        legendStr += castle.getSymbol() + ":    Castle\n"
        legendStr += knight.getSymbol() + ":    Knight\n"
        legendStr += bishop.getSymbol() + ":    Bishop\n"
        legendStr += queen.getSymbol() + ":    Queen\n"
        legendStr += king.getSymbol() + ":    King\n"
        return legendStr

    """Set all the pieces back where they belong"""
    def resetBoard(self):
        for i in range(0,8):
            whitePawn = Pawn("white")
            blackPawn = Pawn("black")
            self.setPiece(self.coord(i, 1), whitePawn)
            self.setPiece(self.coord(i, 6), blackPawn)

        whiteCastleLeft = Castle("white")
        whiteCastleRight = Castle("white")
        self.setPiece(self.coord(0, 0), whiteCastleLeft)
        self.setPiece(self.coord(7, 0), whiteCastleRight)

        blackCastleLeft = Castle("black")
        blackCastleRight = Castle("black")
        self.setPiece(self.coord(0, 7), blackCastleLeft)
        self.setPiece(self.coord(7, 7), blackCastleRight)

        whiteKnightLeft = Knight("white")
        whiteKnightRight = Knight("white")
        self.setPiece(self.coord(1, 0), whiteKnightLeft)
        self.setPiece(self.coord(6, 0), whiteKnightRight)

        blackKnightLeft = Knight("black")
        blackKnightRight = Knight("black")
        self.setPiece(self.coord(1, 7), blackKnightLeft)
        self.setPiece(self.coord(6, 7), blackKnightRight)

        whiteBishopLeft = Bishop("white")
        whiteBishopRight = Bishop("white")
        self.setPiece(self.coord(2, 0), whiteBishopLeft)
        self.setPiece(self.coord(5, 0), whiteBishopRight)

        blackBishopLeft = Bishop("black")
        blackBishopRight = Bishop("black")
        self.setPiece(self.coord(2, 7), blackBishopLeft)
        self.setPiece(self.coord(5, 7), blackBishopRight)

        whiteQueen = Queen("white")
        self.setPiece(self.coord(3, 0), whiteQueen)

        blackQueen = Queen("black")
        self.setPiece(self.coord(4, 7), blackQueen)

        whiteKing = King("white")
        self.setPiece(self.coord(4, 0), whiteKing)

        blackKing = King("black")
        self.setPiece(self.coord(3, 7), blackKing)

        self.whiteKing = whiteKing
        self.blackKing = blackKing


    """Check if the game is over. Return 0 = game still in progress. 1 = white win. 2 = black win."""
    def checkMate(self):
        # Check if kings are alive
        if not self.blackKing.alive:
            return 1
        elif not self.whiteKing.alive:
            return 2
        else:
            return 0

    """Try to move a piece"""
    def move(self, a, b, turn):
        # Convert a & b to co-ordinates
        a = self.convertSpace(a)
        b = self.convertSpace(b)
        attacker = self.getPiece(a)
        defender = self.getPiece(b)

        if attacker is None:
            return False

        if (attacker.attemptMove(a, b, defender, self, turn)):
            self.setPiece(a, None)
            self.setPiece(b, attacker)
            if defender is not None:
                defender.die()
            return True

        return False

    """Utility - convert a text string to co-ords"""
    def convertSpace(self, text):
        text = text.upper();
        if (len(text) != 2):
            raise SyntaxError("Cannot convert text string " + text + " to co-ord.")

        coord = {'x': None, 'y': None}
        if (text[0] == "A"):
            coord['x'] = 0
        elif (text[0] == "B"):
            coord['x'] = 1
        elif (text[0] == "C"):
            coord['x'] = 2
        elif (text[0] == "D"):
            coord['x'] = 3
        elif (text[0] == "E"):
            coord['x'] = 4
        elif (text[0] == "F"):
            coord['x'] = 5
        elif (text[0] == "G"):
            coord['x'] = 6
        elif (text[0] == "H"):
            coord['x'] = 7
        else:
            raise SyntaxError("Unrecognizes symbol '" + text[0] + "'")

        if (int(text[1]) < 0 or int(text[1]) > 7):
            raise SyntaxError("Unrecognized value '" + text[1] + "'")
        else:
            coord['y'] = int(text[1]);

        return coord;

    """Utility - get piece from specific space"""
    def getPiece(self, coord):
        return self.spaces[coord['y']][coord['x']]

    """Utility - set piece given coords"""
    def setPiece(self, coord, piece):
        self.spaces[coord['y']][coord['x']] = piece

    """Utility, create a coord"""
    def coord(self, x, y):
        return {'x': x, 'y': y}
