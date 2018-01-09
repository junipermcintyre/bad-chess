# Chess Piece class!
class Piece:
    team = None
    name = "piece"
    alive = True

    def __init__(self, color):
        self.team = color

    def die(self):
        self.alive = False

    def attemptMove(self, a, b, defender, chess, turn):
        if turn is not self.team:
            return False
        else:
            return self.move(a, b, defender, chess)


    def move(self, a, b, defender, map):
        print "Piece stub!"

    def getSymbol(self):
        return "?";
