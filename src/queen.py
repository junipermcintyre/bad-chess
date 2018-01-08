from .piece import Piece
# Queen chess piece
class Queen(Piece):
    name = "queen"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        return False


    def getSymbol(self):
        if self.team is "white":
            return "Q"
        else:
            return "q"
