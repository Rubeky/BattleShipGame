from tkinter import Tk, Label, Button, Frame
from functools import partial
import math
import random

'''
################################################################################
#############################Start of Board#####################################
################################################################################
'''

class Board:
    #self root object with exit linked to closing window
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", exit)

    #Initialising for objects and game logic
    buttonsObjects = [[None]*10 for _ in range(10)]             #List of the objects
    buttonsClicked = [[False]*10 for _ in range(10)]            #If they've been clicked or not
    opponentButtonsObjects = [[None]*10 for _ in range(10)]
    opponentButtonsClicked = [[False]*10 for _ in range(10)]
    textBox = None
    exitButton = None

    #Ship placement variables
    ships = [2, 2, 3, 4, 5] #Edit this to change length of game/types of ships in play
    loading_game = True
    isBoatComplete = True
    currentBoatToPlace = 0
    x = None
    y = None
    #Boat location data hold pointers to each
    shipsLocations = [[False]*10 for _ in range(10)]
    enemyLocations = [[False]*10 for _ in range(10)]


    #Houses main function calls
    def __init__(self):

        #Sets up all objects
        self.setupScreen()

        print("Made it")

        #Placing ships is done in a loop
        while self.loading_game:
            pass


################################################################################
################################################################################


    #Sets up board with all correct variables
    def setupScreen(self):
        #What we play on
        frame1 = Frame(self.root)
        frame1.grid(row = 1, column = 1)

        #Spacer
        frame2 = Frame(self.root, width = 50)
        frame2.grid(row = 1, column = 2)

        #What the opponent plays on
        frame3 = Frame(self.root)
        frame3.grid(row = 1, column = 3)

        #Spacer
        frame4 = Frame(self.root, height = 10)
        frame4.grid(row = 2, column = 1)

        #TextBox that displays last thing that happened
        self.textBox = Label(self.root, bg = "#808080", text = "Hello", width = 50, height = 10)
        self.textBox.grid(row = 3, column = 1)

        self.exitButton = Button(self.root, bg = "Red", text = "Abort", command = lambda:exit())
        self.exitButton.grid(row = 3, column = 2)


        textList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        labels1 = [None]*11
        labels2 = [None]*11
        opponentLabels1 = [None]*11
        opponentLabels2 = [None]*11

        #Setting up borders of the boards, with the alphabet and the numbering
        for i in range(0,10):
            labels1[i + 1] = Button(frame1)
            labels1[i + 1].config(text = str(i + 1), width = 5, height = 3)
            labels1[i + 1].grid(row = 0, column = i + 1)

            labels2[i + 1] = Button(frame1)
            labels2[i + 1].config(text = textList[i], width = 5, height = 3)
            labels2[i + 1].grid(row = i + 1, column = 0)

            opponentLabels1[i + 1] = Button(frame3)
            opponentLabels1[i + 1].config(text = str(i + 1), width = 5, height = 3)
            opponentLabels1[i + 1].grid(row = 0, column = i + 1)

            opponentLabels2[i + 1] = Button(frame3)
            opponentLabels2[i + 1].config(text = textList[i], width = 5, height = 3)
            opponentLabels2[i + 1].grid(row = i + 1, column = 0)

        #Creating all button objects in both grids
        for x in range(0,10):
            for y in range(0,10):
                #Right grid, used for playing moves
                self.buttonsObjects[x][y] = Button(frame1, command = partial(self.playMove,x,y))
                self.buttonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.buttonsObjects[x][y].grid(row = x + 1, column = y + 1)

                #Left grid, used for setting up boats
                self.opponentButtonsObjects[x][y] = Button(frame3, command = partial(self.placeShips,x,y))
                self.opponentButtonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.opponentButtonsObjects[x][y].grid(row = y + 1, column = x + 1)

        self.root.mainloop()


################################################################################
################################################################################


    #Takes boat placement from the player
    ## TODO: Make checks for if boats overlap
    def placeShips(self, x, y):

        #Variables for making sure the placement works
        ShipX  = []
        ShipY  = []
        crossesOver = False

        #Exit function immediately
        if not self.loading_game:
            #Exit function
            return None

        #The final run of this function, sets up rest of game
        if self.currentBoatToPlace == len(self.ships):

            #Locks you out of function
            self.loading_game = False
            self.textBox.config(text = "The game has started!")

            #Set up opponent ships
            self.opponentPlaceShips()
            return None

        #Clearing textbox
        self.textBox.config(text = "")
        #Changing colour of button clicked
        if self.shipsLocations[x][y] == False:
            self.opponentButtonsObjects[x][y].config(bg = "#C0C0C0")

        #Finding first position of the boat
        if self.isBoatComplete:
            if self.shipsLocations[x][y] == False:
                self.isBoatComplete = False

                #Set first position of ship
                self.x = x
                self.y = y

        #Checking against length, and setting them to be placed if suitable
        elif self.shipsLocations[x][y] == False:
            if x - self.x == self.ships[self.currentBoatToPlace] - 1 and y == self.y:
                for i in range(0, self.ships[self.currentBoatToPlace]):
                    if not self.shipsLocations[self.x + i][y]:
                        ShipX.append(self.x + i)
                        ShipY.append(y)
                    else:
                        crossesOver = True

            elif y - self.y == self.ships[self.currentBoatToPlace] - 1 and x == self.x:
                for i in range(0, self.ships[self.currentBoatToPlace]):
                    if not self.shipsLocations[x][self.y + i]:
                        ShipX.append(x)
                        ShipY.append(self.y + i)
                    else:
                        crossesOver = True

            elif x - self.x == -self.ships[self.currentBoatToPlace] + 1 and y == self.y:
                for i in range(0, self.ships[self.currentBoatToPlace]):
                    if not self.shipsLocations[self.x - i][y]:
                        ShipX.append(self.x - i)
                        ShipY.append(y)
                    else:
                        crossesOver = True

            elif y - self.y == -self.ships[self.currentBoatToPlace] + 1 and x == self.x:
                for i in range(0, self.ships[self.currentBoatToPlace]):
                    if not self.shipsLocations[x][self.y - i]:
                        ShipX.append(x)
                        ShipY.append(self.y - i)
                    else:
                        crossesOver = True

            #Stops boats that havent been placed properly based on boat length
            else:
                self.textBox.config(text = ("You're looking for a place that is " + str(self.ships[self.currentBoatToPlace]) + " away"))
                self.opponentButtonsObjects[x][y].config(bg = "#FFFFFF")
                self.opponentButtonsObjects[self.x][self.y].config(bg = "#FFFFFF")
                self.currentBoatToPlace -= 1

            #Places boat in if it hasn't crossed over another
            if not crossesOver:
                for i in range(0, len(ShipX)):
                    self.shipsLocations[ShipX[i]][ShipY[i]] = True
                    self.opponentButtonsObjects[ShipX[i]][ShipY[i]].config(bg = "green")
            else:
                self.textBox.config(text = ("Please don't overlap boats!"))
                self.opponentButtonsObjects[x][y].config(bg = "#FFFFFF")
                self.opponentButtonsObjects[self.x][self.y].config(bg = "#FFFFFF")
                self.currentBoatToPlace -= 1

            #Getting to next boat
            self.isBoatComplete = True
            self.currentBoatToPlace += 1


################################################################################
################################################################################


    #Sets up their board by random
    def opponentPlaceShips(self):
        #Variables for making sure the placement works
        whichShip = 0
        isImpossible = 0

        while whichShip < len(self.ships) and isImpossible < 5000:
            ShipX  = []
            ShipY  = []
            crossesOver = False

            #Generate random number
            randNumb = random.randint(1,2)

            if randNumb == 1:           #Horizontal
                x = random.randint(0,9 - self.ships[whichShip])
                y = random.randint(0,9)

                for i in range(0, self.ships[whichShip]):
                    if not self.enemyLocations[x + i][y]:
                        ShipX.append(x + i)
                        ShipY.append(y)
                    else:
                        crossesOver = True

            else:         #Vertical
                x = random.randint(0,9)
                y = random.randint(0,9 - self.ships[whichShip])

                for i in range(0, self.ships[whichShip]):
                    if not self.enemyLocations[x][y + i]:
                        ShipX.append(x)
                        ShipY.append(y + i)
                    else:
                        crossesOver = True

            #Places boat in if it hasn't crossed over another
            if not crossesOver:
                for i in range(0, len(ShipX)):
                    self.enemyLocations[ShipX[i]][ShipY[i]] = True
                    self.buttonsObjects[ShipX[i]][ShipY[i]].config(bg = "#A00000")
            else:
                self.textBox.config(text = ("Please don't overlap boats!"))

                whichShip -= 1
                isImpossible += 1

            #Getting to next boat
            self.isBoatComplete = True
            whichShip += 1


################################################################################
################################################################################


    #Takes move from player (via the buttons)
    def playMove(self, x, y):
        return None

        '''Pseudocode
        if not self.buttonsClicked[x-1][y-1]:
            change colour of button
            set them as clicked
            if self.opponentPlaceShips[x][y]:
                mark it as hit?
                set text to reflect that it was hit
                maybe say how many ships are left?
                if sunk, say ship sunk!
        '''
        '''Previous function
        self.boatPlacedButton = True
        if not self.buttonsClicked[x-1][y-1]:
            #Changing colour of button clicked
            self.buttonsObjects[x][y].config(bg = "#808080")
            self.buttonsClicked[x-1][y-1] = True
            #TODO: Check if it hits etc
        else:
            self.textBox.config(text = "You already pressed this")

        #Opponent plays move
        self.opponentMove()
        '''


################################################################################
################################################################################


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

################################################################################
################################################################################

    #Returns state of the game
    def isComplete(self):
        pass

'''
################################################################################
##############################End of Board######################################
################################################################################
'''

#Not within Class Board
gameBoard = Board()
