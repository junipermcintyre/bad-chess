from .piece import Piece
# King chess piece
class King(Piece):
    name = "queen"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        return False


    def getSymbol(self):
        if self.team is "white":
            return "K"
        else:
            return "k"
