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
    oppositeButtonsObjects = [[None]*10 for _ in range(10)]
    oppositeButtonsClicked = [[False]*10 for _ in range(10)]
    textBox = None
    exitButton = None

    #Ship placement variables
    ships = [2, 2, 3, 4, 5] #Edit this to change length of game/types of ships in play
    loading_game = True
    isBoatComplete = True
    currentBoatToPlace = 0
    x = None
    y = None
    #Boat location data , true is the location of part of a boat
    shipsLocations = [[False]*10 for _ in range(10)]
    enemyLocations = [[False]*10 for _ in range(10)]

    playerHits = 0
    opponentHits = 0
    gameOver = False

    #Houses main function calls
    def __init__(self):
        #Sets up all objects
        self.setupScreen()

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
        self.exitButton.grid(row = 3, column = 3)


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
                self.oppositeButtonsObjects[x][y] = Button(frame3, command = partial(self.placeShips,x,y))
                self.oppositeButtonsObjects[x][y].config(textvariable = " ", width = 5, height = 3)
                self.oppositeButtonsObjects[x][y].grid(row = y + 1, column = x + 1)

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
            self.oppositeButtonsObjects[x][y].config(bg = "#C0C0C0")

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
                self.oppositeButtonsObjects[x][y].config(bg = "SystemButtonFace")
                self.oppositeButtonsObjects[self.x][self.y].config(bg = "SystemButtonFace")
                self.currentBoatToPlace -= 1

            #Places boat in if it hasn't crossed over another
            if not crossesOver:
                for i in range(0, len(ShipX)):
                    self.shipsLocations[ShipX[i]][ShipY[i]] = True
                    self.oppositeButtonsObjects[ShipX[i]][ShipY[i]].config(bg = "green")
            else:
                self.textBox.config(text = ("Please don't overlap boats!"))
                self.oppositeButtonsObjects[x][y].config(bg = "SystemButtonFace")
                self.oppositeButtonsObjects[self.x][self.y].config(bg = "SystemButtonFace")
                self.currentBoatToPlace -= 1

            #Getting to next boat
            self.isBoatComplete = True
            self.currentBoatToPlace += 1


################################################################################
################################################################################


    #Sets up their board by random
    def opponentPlaceShips(self):
        #Variables for making sure the placement works
        currentBoatToPlace = 0
        isImpossible = 0

        while currentBoatToPlace < len(self.ships) and isImpossible < 5000:
            ShipX  = []
            ShipY  = []
            crossesOver = False

            #Generate random number
            randNumb = random.randint(1,2)

            if randNumb == 1:           #Horizontal
                x = random.randint(0,9 - self.ships[currentBoatToPlace] + 1)
                y = random.randint(0,9)

                for i in range(0, self.ships[currentBoatToPlace]):
                    if not self.enemyLocations[x + i][y]:
                        ShipX.append(x + i)
                        ShipY.append(y)
                    else:
                        crossesOver = True

            else:                       #Vertical
                x = random.randint(0,9)
                y = random.randint(0,9 - self.ships[currentBoatToPlace] + 1)

                for i in range(0, self.ships[currentBoatToPlace]):
                    if not self.enemyLocations[x][y + i]:
                        ShipX.append(x)
                        ShipY.append(y + i)
                    else:
                        crossesOver = True

            #Places boat in if it hasn't crossed over another
            if not crossesOver:
                for i in range(0, len(ShipX)):
                    self.enemyLocations[ShipX[i]][ShipY[i]] = True

                    #For debugging
                    #self.buttonsObjects[ShipX[i]][ShipY[i]].config(bg = "#A00000")
            else:
                currentBoatToPlace -= 1
                isImpossible += 1

            #Getting to next boat
            self.isBoatComplete = True
            currentBoatToPlace += 1


################################################################################
################################################################################


    #Takes move from player (via the buttons)
    def playMove(self, x, y):
        if not self.gameOver:
            self.textBox.config(text = "")
            self.buttonsClicked[x-1][y-1] = True
            self.buttonsObjects[x][y].config(bg = "#808080")

            if self.enemyLocations[x][y]:
                self.buttonsObjects[x][y].config(bg = "Red")
                self.textBox.config(text = "Enemy hit!")
                self.playerHits += 1


            self.opponentMove()

        if self.whoWon() == 1:
            self.textBox.config(text = "Congratulations, you won!")

################################################################################
################################################################################


    #Plays opponent moves
    #if no hits made: random movements
    #if one hit made: try sink ship **TODO**
    def opponentMove(self):
        noMoveMade = True

        while noMoveMade:
            x = random.randint(0,9)
            y = random.randint(0,9)

            if not self.oppositeButtonsClicked[x][y]:
                noMoveMade = False
                self.oppositeButtonsClicked[x][y] = True

                if self.shipsLocations[x][y]:
                    self.textBox.config(text = "Enemy hit your boat!")
                    self.opponentHits += 1


        if self.whoWon() == 2:
            self.textBox.config(text = "Oh no, all your ships were sunk!")



################################################################################
################################################################################


    #Returns state of the game
    #0 = not won yet
    #1 = player won
    #2 = opponent won
    def whoWon(self):
        numberOfTilesToHit = sum(self.ships)

        self.textBox.config(text = str(self.opponentHits) + " " + str(self.playerHits))

        if self.opponentHits == numberOfTilesToHit:
            self.gameOver = True
            return 2
        elif self.playerHits == numberOfTilesToHit:
            self.gameOver = True
            return 1
        else:
            return 0


'''
################################################################################
##############################End of Board######################################
################################################################################
'''

#Not within Class Board
gameBoard = Board()
