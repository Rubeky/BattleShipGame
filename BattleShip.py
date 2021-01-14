from tkinter import Tk, Label, Button, Frame
from functools import partial
import math

class Board:
    #Initialising both board and board logic
    buttonsObjects = [[None]*11 for _ in range(11)]
    buttonsClicked = [[False]*10 for _ in range(10)]
    opponentButtonsObjects = [[None]*11 for _ in range(11)]
    opponentButtonsClicked = [[False]*10 for _ in range(10)]


    def __init__(self, master):
        self.setupScreen()
        #Places all ships including opponent ships
        #self.placeShips()

    #Sets up board with all correct variables
    def setupScreen(self):
        frame1 = Frame(root)
        frame1.grid(row = 1, column = 1)

        frame2 = Frame(root, width = 50)
        frame2.grid(row = 1, column = 2)

        frame3 = Frame(root)
        frame3.grid(row = 1, column = 3)

        frame4 = Frame(root, height = 100)
        frame4.grid(row = 2, column = 1)

        textList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        for i in range(0,10):
            self.buttonsObjects[i + 1][0] = Button(frame1)
            self.buttonsObjects[i + 1][0].config(text = str(i + 1), width = 5, height = 3)
            self.buttonsObjects[i + 1][0].grid(row = 0, column = i + 1)

            self.buttonsObjects[0][i + 1] = Button(frame1)
            self.buttonsObjects[0][i + 1].config(text = textList[i], width = 5, height = 3)
            self.buttonsObjects[0][i + 1].grid(row = i + 1, column = 0)

            self.opponentButtonsObjects[i + 1][0] = Button(frame3)
            self.opponentButtonsObjects[i + 1][0].config(text = str(i + 1), width = 5, height = 3)
            self.opponentButtonsObjects[i + 1][0].grid(row = 0, column = i + 1)

            self.opponentButtonsObjects[0][i + 1] = Button(frame3)
            self.opponentButtonsObjects[0][i + 1].config(text = textList[i], width = 5, height = 3)
            self.opponentButtonsObjects[0][i + 1].grid(row = i + 1, column = 0)

        for x in range(1,11):
            for y in range(1,11):
                self.buttonsObjects[x][y] = Button(frame1, command = partial(self.playMove,x,y))
                self.buttonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.buttonsObjects[x][y].grid(row = x, column = y)


                self.opponentButtonsObjects[x][y] = Button(frame3)
                self.opponentButtonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.opponentButtonsObjects[x][y].grid(row = y, column = x)

        root.mainloop()


    #Takes move from player (via the buttons)
    def playMove(self,x,y):
        if self.checkMove(x,y):
            #Changing colour of button clicked
            self.buttonsObjects[x][y].config(bg = "#808080")
            self.buttonsClicked[x-1][y-1] = True
        else:
            print("Button already pressed")

    #Returns validity of a move
    def checkMove(self,x,y):
        return not self.buttonsClicked[x-1][y-1]

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
