from .piece import Piece
# Pawn chess piece
class Pawn(Piece):
    name = "pawn"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        xCheck = False
        yCheck = False

        if (defender is not None):
            if defender.team is not self.team:
                if b['x'] + 1 == a['x'] or b['x'] - 1 == a['x']: # Diagnol
                    xCheck = True
        else:
            if b['x'] == a['x']: # straight
                xCheck = True

        if self.team is "white": #Go down (white on top) 0->7, 0v7
            if b['y'] == a['y'] + 1:
                yCheck = True
        else:
            if b['y'] == a['y'] - 1:
                yCheck = True

        return xCheck and yCheck

    def getSymbol(self):
        if self.team is "white":
            return "P"
        else:
            return "p"
