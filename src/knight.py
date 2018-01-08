from .piece import Piece
# Knight chess piece
class Knight(Piece):
    name = "knight"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        return False


    def getSymbol(self):
        if self.team is "white":
            return "N"
        else:
            return "n"
