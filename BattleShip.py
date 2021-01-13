from tkinter import Tk, Label, Button
from functools import partial
import math

class Board:
    #Initialising both board and board logic
    buttonsObjects = [[None]*10 for _ in range(10)]
    buttonsClicked = [[False]*10 for _ in range(10)]
    opponentButtonsObjects = [[None]*10 for _ in range(10)]
    opponentButtonsClicked = [[False]*10 for _ in range(10)]


    def __init__(self, master):
        self.setupScreen()
        self.opponentSetup()

    #Sets up board with all correct variables
    def setupScreen(self):
        for x in range(0,10):
            for y in range(0,10):
                self.buttonsObjects[x][y] = Button(root, command = partial(self.playMove,x,y))
                self.buttonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.buttonsObjects[x][y].grid(row = x, column = y)

    #Takes move from player (via the buttons)
    def playMove(self,x,y):
        if self.checkMove(x,y):
            #Changing colour of button clicked
            self.buttonsObjects[x][y].config(bg = "#808080")
            self.buttonsClicked[x][y] = True
        else:
            print("Button already pressed")

    #Returns validity of a move
    def checkMove(self,x,y):
        return not self.buttonsClicked[x][y]

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
