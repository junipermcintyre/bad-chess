from .piece import Piece
# Bishop chess piece
class Bishop(Piece):
    name = "bishop"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        return False


    def getSymbol(self):
        if self.team is "white":
            return "B"
        else:
            return "b"
