from src.chess import Chess

# Initial
game = Chess()
print game.printBoard()
print game.printLegend()

turn = "white"
while game.checkMate() == 0:
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

    print game.printBoard()

    if turn is "white":
        turn = "black"
    else:
        turn = "white"
