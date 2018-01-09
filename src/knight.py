from .piece import Piece
# Knight chess piece
class Knight(Piece):
    name = "knight"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        # The difference in x must be 1 if the difference in y is 2
        # The difference in x must be 2 if the difference in y is 1
        yDiff = abs(a['y'] - b['y'])            # only 1 & 2
        if yDiff is not 1 and yDiff is not 2:
            return False

        xDiff = abs(a['x'] - b['x'])            # only 1 & 2
        if xDiff is not 1 and xDiff is not 2:
            return False

        # One or the other check
        if yDiff is 1 and xDiff is not 2:
            return False
        elif yDiff is 2 and xDiff is not 1:
            return False

        # Check final spot
        finalSpace = map.getPiece(b)
        if finalSpace is not None:
            if finalSpace.team is self.team:
                return False

        return True     # all good!


    def getSymbol(self):
        if self.team is "white":
            return "N"
        else:
            return "n"
