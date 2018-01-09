from .piece import Piece
# Queen chess piece
class Queen(Piece):
    name = "queen"

    """a and b are coords"""
    def move(self, a, b, defender, map):
        # If it's not moving like a castle, and its not moving like a bishop, then dont let it go through
        # Diagnol means the difference in 'x' must be equal to the difference in 'y'
        xDiff = abs(a['x'] - b['x'])
        yDiff = abs(a['y'] - b['y'])
        bishopCheck = True
        if xDiff is not yDiff:
            bishopCheck = False

        castleCheck = True
        if (a['x'] is not b['x'] and a['y'] is not b['y']):
            castleCheck = False

        if (not castleCheck) and (not bishopCheck): # How is it moving lol
            return False

        # Check everything in between now that we know the move is OK
        startX = a['x']
        startY = a['y']
        while (startX is not b['x'] or startY is not b['y']):

            if startX < b['x']:
                startX = startX+1
            elif startX > b['x']:
                startX = startX-1

            if startY < b['y']:
                startY = startY+1
            elif startY > b['y']:
                startY = startY-1

            # Check if there's a piece here as long as it's not the final space
            if (startX is not b['x']) or (startY is not b['y']):
                if map.getPiece({'x': startX, 'y': startY}) is not None:
                    return False

        # Check final space (for friendlies)
        finalSpace = map.getPiece(b)
        if finalSpace is not None:
            if finalSpace.team is self.team:
                return False

        return True


    def getSymbol(self):
        if self.team is "white":
            return "Q"
        else:
            return "q"
