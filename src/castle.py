from .piece import Piece
# Castle chess piece
class Castle(Piece):
    name = "castle"

    """a and b are coords"""
    def move(self, a, b, defender, map):

        # x can change, or y can change, but not both. Can't go past other objects too.
        if (a['x'] is not b['x'] and a['y'] is not b['y']):
            return False

        # Make sure nothing in the way
        smallX = a['x']
        bigX = b['x']
        if (b['x'] < a['x']):
            smallX = b['x']
            bigX = a['x']

        smallY = a['y']
        bigY = b['y']
        if (b['y'] < a['y']):
            smallY = b['y']
            bigY = a['y']

        for i in range(smallX+1, bigX):
            if (map.getPiece({'x': i, 'y': smallY}) is not None):  # if not empty
                return False

        for j in range(smallY+1, bigY):
            if (map.getPiece({'x': smallX, 'y': j}) is not None): # if not empty
                return False

        # Check final piece
        piece = map.getPiece(b)
        if piece is not None:
            if piece.team is self.team:
                return False            # Can't step on own piece

        return True


    def getSymbol(self):
        if self.team is "white":
            return "C"
        else:
            return "c"
