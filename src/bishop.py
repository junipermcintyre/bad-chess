from .piece import Piece
# Bishop chess piece
class Bishop(Piece):
    name = "bishop"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        # Diagnol means the difference in 'x' must be equal to the difference in 'y'
        xDiff = abs(a['x'] - b['x'])
        yDiff = abs(a['y'] - b['y'])
        if xDiff is not yDiff:
            return False

        # Make sure all the spaces between a and b are empty
        startX = a['x']
        startY = a['y']
        while (startX is not b['x'] and startY is not b['y']):
            if startX < b['x']:
                startX = startX+1
            elif startX > b['x']:
                startX = startX-1

            if startY < b['y']:
                startY = startY+1
            elif startY > b['y']:
                startY = startY-1

            # Check if there's a piece here as long as it's not the final space
            if startX is not b['x'] and startY is not b['y']:
                if map.getPiece({'x': startX, 'y': startY}) is not None:
                    return False

        # Check final space
        finalSpace = map.getPiece(b)
        if finalSpace is not None:
            if finalSpace.team is self.team:
                return False

        return True


    def getSymbol(self):
        if self.team is "white":
            return "B"
        else:
            return "b"
