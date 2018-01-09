from src.chess import Chess

# Initial
game = Chess()
print game.printBoard()
print game.printLegend()

turn = "white"
moves = []
while game.checkMate() is 0:
    print "Player's turn - " + turn
    coords = raw_input("Enter move [X# Y#]: ")
    while len(coords) != 5:
        coords = raw_input("Respect syntax - Enter move [X# Y#]: ")
    start = coords[:2]
    end = coords[3:]

    while not game.move(start, end, turn):
        coords = raw_input("Move invalid - Enter move [X# Y#]: ")
        while len(coords) != 5:
            coords = raw_input("Respect syntax - Enter move [X# Y#]: ")
        start = coords[:2]
        end = coords[3:]
        moves.append(coords)

    print game.printBoard()

    if turn is "white":
        turn = "black"
    else:
        turn = "white"

winner = game.checkMate()
print game.printBoard()
if winner is 1:
    print "Congratulations - white player has taken the black king!"
elif winner is 2:
    print "Congratulations - black player has taken the white king!"
else:
    print "Draw - no player wins"
