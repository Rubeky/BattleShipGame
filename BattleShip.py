from tkinter import Tk, Label, Button
from functools import partial
import math

class Board:
    buttonsObjects = [[None]*10 for _ in range(10)]
    buttonsClicked = [[None]*10 for _ in range(10)]
    opponentButtonsObjects = [[None]*10 for _ in range(10)]
    opponentButtonsClicked = [[None]*10 for _ in range(10)]


    def __init__(self, master):
        for x in range(0,10):
            for y in range(0,10):
                self.buttonsClicked[x][y] = False
        self.setupScreen()
        self.opponentSetup()
        print(self.buttonsClicked)

    #Sets up board with all correct variables
    def setupScreen(self):
        for x in range(0,10):
            for y in range(0,10):
                self.buttonsObjects[x][y] = Button(root, command = partial(self.playMove,x,y))
                self.buttonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.buttonsObjects[x][y].grid(row = x, column = y)

    #Takes move from player (via the buttons)
    def playMove(self,x,y):
        #if self.checkMove(x,y):
        self.buttonsClicked[x][y] = True
        print(self.buttonsClicked)

    #Returns validity of a move
    def checkMove(self,x,y):
        return True

    #Sets up their board by random
    #(making sure no ships overlap)
    def opponentSetup(self):
        pass

    #Does a random move for the opponent
    def opponentMove(self):
        pass

    #Returns state of the game
    def isComplete(self):
        pass

root = Tk()
gameBoard = Board(root)
root.mainloop()
