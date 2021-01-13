import maths

class Board:
    buttonsObjects = [[]]
    buttonsClicked = [[]]
    opponentButtonsObjects = [[]]
    opponentButtonsClicked = [[]]


    def __init__():
        setupScreen()
        opponentSetup()

    #Sets up board with all correct variables
    def setupScreen():
        pass

    #Takes move from player (via the buttons)
    def playMove(x,y):
        if checkMove(x,y):
            buttonsClicked[x][y] = 1

    #Returns validity of a move
    def checkMove(x,y):
        pass

    #Sets up their board by random
    #(making sure no ships overlap)
    def opponentSetup():
        pass

    #Does a random move for the opponent
    def opponentMove():
        pass

    #Returns state of the game
    def isComplete():
        pass


gameBoard = Board()
