from .piece import Piece
# Pawn chess piece
class Pawn(Piece):
    name = "pawn"
    hasMoved = False        # Pawns can move two spaces for their first move

    """a and b are coords"""
    def move(self, a, b, defender, map):
        xCheck = False
        yCheck = False

        if (defender is not None):
            if defender.team is not self.team:
                if b['x'] + 1 is a['x'] or b['x'] - 1 is a['x']: # Diagnol
                    xCheck = True
        else:
            if b['x'] is a['x']: # straight
                xCheck = True

        if self.team is "white": #Go down (white on top) 0->7, 0v7
            if b['y'] is a['y'] + 1:
                yCheck = True
            elif b['y'] is a['y'] + 2 and not self.hasMoved:    # First move can be two
                yCheck = True
        else:
            if b['y'] is a['y'] - 1:
                yCheck = True
            elif b['y'] is a['y'] - 2 and not self.hasMoved:    # First move can be two
                yCheck = True

        if xCheck and yCheck:
            self.hasMoved = True

        return xCheck and yCheck

    def getSymbol(self):
        if self.team is "white":
            return "P"
        else:
            return "p"
