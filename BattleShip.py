from tkinter import Tk, Label, Button, Frame
from functools import partial
import math

class Board:
    #Initialising for objects and game logic
    buttonsObjects = [[None]*11 for _ in range(11)]
    buttonsClicked = [[False]*10 for _ in range(10)]
    opponentButtonsObjects = [[None]*11 for _ in range(11)]
    opponentButtonsClicked = [[False]*10 for _ in range(10)]
    textBox = None
    exitButton = None

    #Ship placement variables
    ships = [2, 2, 3, 4, 5] #Edit this to change length of game/types of ships in play
    loading_game = True
    boatPlacedButton = False
    currentBoatToPlace = 0

    #Used while game is running
    played = False


    def __init__(self, master):
        self.loading_game = True
        self.setupScreen()
        #placing ships is done in a loop
        while self.loading_game:
            pass

        #Placing all opponent ships
        self.opponentPlaceShips()

        #Game loop
        while not self.isComplete():
            #Waiting for player to do move
            while(not self.played):
                self.played = False

            #Have opponent play move
            self.opponentMove()

        #Winning screen?

    #Sets up board with all correct variables
    def setupScreen(self):
        frame1 = Frame(root)
        frame1.grid(row = 1, column = 1)

        frame2 = Frame(root, width = 50)
        frame2.grid(row = 1, column = 2)

        frame3 = Frame(root)
        frame3.grid(row = 1, column = 3)

        frame4 = Frame(root, height = 10)
        frame4.grid(row = 2, column = 1)

        self.textBox = Label(root, bg = "#808080", text = "Hello", width = 50, height = 10)
        self.textBox.grid(row = 3, column = 1)

        self.exitButton = Button(root, bg = "Red", text = "Abort", command = lambda:self.exit_window())
        self.exitButton.grid(row = 3, column = 2)


        textList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        #Setting up borders of the boards, with the alphabet and the numbering
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

        #Creating all button objects in a grid
        for x in range(1,11):
            for y in range(1,11):
                self.buttonsObjects[x][y] = Button(frame1, command = partial(self.playMove,x,y))
                self.buttonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.buttonsObjects[x][y].grid(row = x, column = y)


                self.opponentButtonsObjects[x][y] = Button(frame3, command = partial(self.placeShips,x,y))
                self.opponentButtonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.opponentButtonsObjects[x][y].grid(row = y, column = x)

        root.mainloop()


    #Takes boat placement from the player
    #TODO: make boat placement work
    def placeShips(self, x, y):
        self.boatPlacedButton = True

        #Changing colour of button clicked
        self.opponentButtonsObjects[x][y].config(bg = "#C0C0C0")

        '''
        If isBoatComplete = true
            #If currentBoatToPlace == self.ships.length()
                #self.loading_game = False
                #return None
            #currentBoatToPlace++
            #check if x and y are free and place
        #else
            #check if it's the correct distance away:
                place ship
            if not correct distance:
                self.textBox.config(text = ("You're looking for a place that is " + self.ships[currentBoatToPlace] + " away"))
        '''



    #Takes move from player (via the buttons)
    def playMove(self, x, y):
        self.boatPlacedButton = True
        if not self.buttonsClicked[x-1][y-1]:
            #Changing colour of button clicked
            self.buttonsObjects[x][y].config(bg = "#808080")
            self.buttonsClicked[x-1][y-1] = True
            #TODO: Check if it hits etc
        else:
            self.textBox.config(text = "You already pressed this")

    #Sets up their board by random
    #(making sure no ships overlap)
    def opponentPlaceShips(self):
        '''
        while shipsPlaced < self.ships():
            generate random x and y
            if available:
                generate random (n, w, e, or s)
                if it doesnt interfere with other ship:
                    place ship in (all parts)
                    #colour board red for testing purposes
                else:
                    delete whole ship
            else:
                delete whole ship
        '''

    #Does a random move for the opponent or if a ship
    # has been hit, this triggers an algorithm
    def opponentMove(self):
        '''
        if not currentTarget:
            random x and y
        else:
            try north, south, east, west depending on hits
            (use a stack??)

        '''

    #Returns state of the game
    def isComplete(self):
        pass

    #deletes instance of game
    def exit_window(self):
        root.destroy()
        exit()

root = Tk()
gameBoard = Board(root)
