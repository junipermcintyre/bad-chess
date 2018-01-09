from .piece import Piece
# King chess piece
class King(Piece):
    name = "queen"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        # Kings can move... one space. Any direction. Thus...
        # The maximum difference in xs must be one
        # The maximum difference in ys must be one
        # The maximum total difference between the two must be two
        # The minimum total difference between the two must be one (something must've moved)

        diffX = abs(a['x'] - b['x'])
        diffY = abs(a['y'] - b['y'])

        if diffX > 1 or diffY > 1:  # Can't move more than 1 in x/y
            return False

        if diffX + diffY > 2 or diffX + diffY < 1: # in total, can't move more than 2 or less than 1
            return False

        # Check if the space if friendly (can't move)
        finalSpace = map.getPiece(b)
        if finalSpace is not None:
            if finalSpace.team is self.team:
                return False


        return True


    def getSymbol(self):
        if self.team is "white":
            return "K"
        else:
            return "k"
