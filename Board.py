import posixpath
from enum import Enum

from Deck import *

from Team import *


class Type(Enum):
    START = "Start"
    UNSAFE = "Unsafe"
    SAFE = "Safe"
    HOME = "Home"
    REDEND = "RedEnd"
    YELLOWEND = "YellowEnd"
    BLUEEND = "BlueEnd"
    GREENEND = "GreenEnd"


class Inside(Enum):
    EMPTY = 0
    HASRED = 1
    HASYELLOW = 2
    HASBLUE = 3
    HASGREEN = 4

class Tile:
    def __init__(self, inhabited, variation, position):
        self.inhabited = inhabited
        self.variation = variation
        self.position = position
        self.item = []
        self.coords = [0,0]

    def __str__(self):
        return str(self.inhabited)

    def setCoords(x,y):
        coords = [x,y]

    def getCoords(self):
        return self.coords
class Board:

    matrix = [Tile(inhabited=Inside.EMPTY, variation=Type.UNSAFE, position=i) for i in range(60)]

    safeBlue = [Tile(inhabited=Inside.EMPTY, variation=Type.SAFE, position=i) for i in range(4)]
    safeRed = [Tile(inhabited=Inside.EMPTY, variation=Type.SAFE, position=i) for i in range(4)]
    safeYellow = [Tile(inhabited=Inside.EMPTY, variation=Type.SAFE, position=i) for i in range(4)]
    safeGreen = [Tile(inhabited=Inside.EMPTY, variation=Type.SAFE, position=i) for i in range(4)]


    theDeck = Deck()

    redTeam = Team("Red", 4, 2)
    blueTeam = Team("Blue", 19, 17)
    yellowTeam = Team("Yellow", 34, 32)
    greenTeam = Team("Green", 49, 47)

    matrix[2].variation = Type.REDEND
    matrix[17].variation = Type.BLUEEND
    matrix[32].variation = Type.YELLOWEND
    matrix[47].variation = Type.GREENEND

    def __init__(self):
        self.theDeck.shuffleDeck()

    def turn(self, color, card, choice):

        currentCard = card

        if self.redTeam.inHome == 4 or self.blueTeam.inHome == 4 or self.greenTeam.inHome == 4 or self.yellowTeam.inHome == 4:
            print("Game over! 4 in home!")
            exit(0)

        if currentCard == 13:
            return self.sorry(color)


        chosenPiece = choice

        if color == "Red":


            if self.redTeam.pieces[chosenPiece - 1].coords == pos.HOME:
                print("In Home!")
                return True

            if self.redTeam.pieces[chosenPiece - 1] in self.redTeam.homeStrip:
                return self.moveHome(color, self.redTeam.pieces[chosenPiece - 1].coords, currentCard, chosenPiece)

            startCoord = self.redTeam.pieces[chosenPiece - 1].coords
            if startCoord == pos.START:
                if currentCard == 1 or currentCard == 2:
                    destination = self.redTeam.startCoords
                    if self.redTeam.pieceAt(destination):
                        print("Cannot move, piece already there")
                        return False
                    self.redTeam.leaveStart(chosenPiece - 1)
                else:
                    print("Could not move piece out of start. SORRY!")
                    return False
            else:


                if currentCard != 4:
                    destination = startCoord + currentCard
                    if destination >= 60:
                        destination = 0 + (destination - 60)
                else:
                    destination = startCoord - currentCard
                    if destination < 0:
                        destination = 60 + destination

                if ((startCoord >= 51 and currentCard + startCoord > 62) or (startCoord <= 2 and destination > 2) and currentCard != 4):
                    #return self.homeTransition(color, startCoord, destination - 2, chosenPiece)
                    return self.homeTransition(color, startCoord, currentCard, chosenPiece)

                if self.redTeam.pieceAt(destination):
                    print("Cannot move, piece already there")
                    return False

                self.matrix[startCoord].inhabited = Inside.EMPTY
                self.redTeam.move(startCoord, destination)

            if self.matrix[destination].inhabited == Inside.HASGREEN:
                self.greenTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASBLUE:
                self.blueTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASYELLOW:
                self.yellowTeam.enterStart(destination)

            self.matrix[destination].inhabited = Inside.HASRED


        if color == "Blue":
            startCoord = self.blueTeam.pieces[chosenPiece - 1].coords

            if self.blueTeam.pieces[chosenPiece - 1].coords == pos.HOME:
                print("In Home!")
                return True

            if self.blueTeam.pieces[chosenPiece - 1] in self.blueTeam.homeStrip:
                return self.moveHome(color, self.blueTeam.pieces[chosenPiece - 1].coords, currentCard, chosenPiece)

            if startCoord == pos.START:
                if currentCard == 1 or currentCard == 2:
                    destination = self.blueTeam.startCoords
                    if self.blueTeam.pieceAt(destination):
                        print("Cannot move, piece already there.")
                        return False
                    self.blueTeam.leaveStart(chosenPiece - 1)
                else:
                    print("Could not move piece out of start. SORRY!")
                    return False

            else:

                if currentCard != 4:
                    destination = startCoord + currentCard

                    if destination >= 60:
                        destination = 0 + (destination - 60)

                else:
                    destination = startCoord - currentCard
                    if destination < 0:
                        destination = 59 + destination

                if self.blueTeam.pieceAt(destination):
                    print("Cannot move, piece already there.")
                    return False

                if ((startCoord >= 5 and startCoord <= 17) and destination > 17):
                    #return self.homeTransition(color, startCoord, destination - 17, chosenPiece)
                    return self.homeTransition(color, startCoord, currentCard, chosenPiece)

                self.matrix[startCoord].inhabited = Inside.EMPTY
                self.blueTeam.move(startCoord, destination)

            if self.matrix[destination].inhabited == Inside.HASGREEN:
                self.greenTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASRED:
                self.redTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASYELLOW:
                self.yellowTeam.enterStart(destination)

            self.matrix[destination].inhabited = Inside.HASBLUE


        if color == "Green":
            startCoord = self.greenTeam.pieces[chosenPiece - 1].coords

            if self.greenTeam.pieces[chosenPiece - 1].coords == pos.HOME:
                print("In Home!")
                return True

            if self.greenTeam.pieces[chosenPiece - 1] in self.greenTeam.homeStrip:
                return self.moveHome(color, self.greenTeam.pieces[chosenPiece - 1].coords, currentCard, chosenPiece)

            if startCoord == pos.START:
                if currentCard == 1 or currentCard == 2:
                    destination = self.greenTeam.startCoords
                    if self.greenTeam.pieceAt(destination):
                        print("Cannot move, piece already there")
                        return False
                    self.greenTeam.leaveStart(chosenPiece - 1)
                else:
                    print("Could not move piece out of start. SORRY!")
                    return False

            else:

                if currentCard != 4:
                    destination = startCoord + currentCard
                    if destination >= 60:
                        destination = 0 + (destination - 60)

                else:
                    destination = startCoord - currentCard
                    if destination < 0:
                        destination = 59 + destination

                if ((startCoord >= 35 and startCoord <= 47) and destination > 47):
                    #return self.homeTransition(color, startCoord, destination - 47, chosenPiece)
                    return self.homeTransition(color, startCoord, currentCard, chosenPiece)

                if self.greenTeam.pieceAt(destination):
                    print("Cannot move, piece already there")
                    return False

                self.matrix[startCoord].inhabited = Inside.EMPTY
                self.greenTeam.move(startCoord, destination)

            if self.matrix[destination].inhabited == Inside.HASBLUE:
                self.blueTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASRED:
                self.redTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASYELLOW:
                self.yellowTeam.enterStart(destination)


            self.matrix[destination].inhabited = Inside.HASGREEN


        if color == "Yellow":
            startCoord = self.yellowTeam.pieces[chosenPiece - 1].coords

            if self.yellowTeam.pieces[chosenPiece - 1].coords == pos.HOME:
                print("In Home!")
                return True

            if self.yellowTeam.pieces[chosenPiece - 1] in self.yellowTeam.homeStrip:
                return self.moveHome(color, self.yellowTeam.pieces[chosenPiece - 1].coords, currentCard, chosenPiece)

            if startCoord == pos.START:
                if currentCard == 1 or currentCard == 2:
                    destination = self.yellowTeam.startCoords
                    if self.yellowTeam.pieceAt(destination):
                        print("Cannot move, piece already there")
                        return False
                    self.yellowTeam.leaveStart(chosenPiece - 1)
                else:
                    print("Could not move piece out of start. SORRY!")
                    return False

            else:


                if currentCard != 4:
                    destination = startCoord + currentCard
                    if destination >= 60:
                        destination = 0 + (destination - 60)

                else:
                    destination = startCoord - currentCard
                    if destination < 0:
                        destination = 59 + destination

                if self.yellowTeam.pieceAt(destination):
                    print("Cannot move, piece already there")
                    return False

                if ((startCoord >= 20 and startCoord <= 32) and destination > 32):
                    #return self.homeTransition(color, startCoord, destination - 32, chosenPiece)
                    return self.homeTransition(color, startCoord, currentCard, chosenPiece)

                self.matrix[startCoord].inhabited = Inside.EMPTY
                self.yellowTeam.move(startCoord, destination)

            if self.matrix[destination].inhabited == Inside.HASGREEN:
                self.greenTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASRED:
                self.redTeam.enterStart(destination)
            if self.matrix[destination].inhabited == Inside.HASBLUE:
                self.blueTeam.enterStart(destination)

            self.matrix[destination].inhabited = Inside.HASYELLOW

        return True


    def homeTransition(self, color, startCoord, movement, chosenPiece):
        #print("Hey")

        if color == "Red":
            if self.redTeam.enterHomeStrip(startCoord, movement) == True:
                self.matrix[startCoord].inhabited = Inside.EMPTY
                return True
            else:
                return False

        if color == "Blue":
            if self.blueTeam.enterHomeStrip(startCoord, movement) == True:
                self.matrix[startCoord].inhabited = Inside.EMPTY
                return True
            else:
                return False

        if color == "Green":
            if self.greenTeam.enterHomeStrip(startCoord, movement) == True:
                self.matrix[startCoord].inhabited = Inside.EMPTY
                return True
            else:
                return False

        if color == "Yellow":
            if self.yellowTeam.enterHomeStrip(startCoord, movement) == True:
                self.matrix[startCoord].inhabited = Inside.EMPTY
                return True
            else:
                return False

    def sorry(self, color):
        if color == "Red":
            currIndex = 0
            for piece in self.redTeam.pieces:
                if piece.coords == pos.START:
                    chosenPiece = currIndex
                    break
                currIndex += 1

            if self.redTeam.inStart <= 0:
                print("No pieces in start. SORRY!")
                return False
            else:
                currIndex = 0
                escape = False
                for tile in self.matrix:
                    if tile.inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(currIndex)
                        self.redTeam.move(pos.START, currIndex)
                        self.redTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASRED
                        escape = True
                        break
                    if tile.inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(currIndex)
                        self.redTeam.move(pos.START, currIndex)
                        self.redTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASRED
                        escape = True
                        break
                    if tile.inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(currIndex)
                        self.redTeam.move(pos.START, currIndex)
                        self.redTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASRED
                        escape = True
                        break
                    currIndex += 1
                if escape == False:
                    print("No other pieces on board. SORRY!")
                return False

        if color == "Green":
            currIndex = 0
            for piece in self.greenTeam.pieces:
                if piece.coords == pos.START:
                    chosenPiece = currIndex
                    break
                currIndex += 1

            if self.greenTeam.inStart <= 0:
                print("No pieces in start. SORRY!")
                return False
            else:
                currIndex = 0
                escape = False
                for tile in self.matrix:
                    if tile.inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(currIndex)
                        self.greenTeam.move(pos.START, currIndex)
                        self.greenTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASGREEN
                        escape = True
                        break
                    if tile.inhabited == Inside.HASRED:
                        self.redTeam.enterStart(currIndex)
                        self.greenTeam.move(pos.START, currIndex)
                        self.greenTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASGREEN
                        escape = True
                        break
                    if tile.inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(currIndex)
                        self.greenTeam.move(pos.START, currIndex)
                        self.greenTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASGREEN
                        escape = True
                        break
                    currIndex += 1
                if escape == False:
                    print("No other pieces on board. SORRY!")
                return False

        if color == "Yellow":
            currIndex = 0
            for piece in self.yellowTeam.pieces:
                if piece.coords == pos.START:
                    chosenPiece = currIndex
                    break
                currIndex += 1

            if self.yellowTeam.inStart <= 0:
                print("No pieces in start. SORRY!")
                return False
            else:
                currIndex = 0
                escape = False
                for tile in self.matrix:
                    if tile.inhabited == Inside.HASRED:
                        self.redTeam.enterStart(currIndex)
                        self.yellowTeam.move(pos.START, currIndex)
                        self.yellowTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASYELLOW
                        escape = True
                        break
                    if tile.inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(currIndex)
                        self.yellowTeam.move(pos.START, currIndex)
                        self.yellowTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASYELLOW
                        escape = True
                        break
                    if tile.inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(currIndex)
                        self.yellowTeam.move(pos.START, currIndex)
                        self.yellowTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASYELLOW
                        escape = True
                        break
                    currIndex += 1
                if escape == False:
                    print("No other pieces on board. SORRY!")
                return False

        if color == "Blue":
            currIndex = 0
            for piece in self.blueTeam.pieces:
                if piece.coords == pos.START:
                    chosenPiece = currIndex
                    break
                currIndex += 1

            if self.blueTeam.inStart <= 0:
                print("No pieces in start. SORRY!")
                return False
            else:
                currIndex = 0
                escape = False
                for tile in self.matrix:
                    if tile.inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(currIndex)
                        self.blueTeam.move(pos.START, currIndex)
                        self.blueTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASBLUE
                        escape = True
                        break
                    if tile.inhabited == Inside.HASRED:
                        self.redTeam.enterStart(currIndex)
                        self.blueTeam.move(pos.START, currIndex)
                        self.blueTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASBLUE
                        escape = True
                        break
                    if tile.inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(currIndex)
                        self.blueTeam.move(pos.START, currIndex)
                        self.greenTeam.inStart -= 1
                        self.matrix[currIndex].inhabited = Inside.HASBLUE
                        escape = True
                        break
                    currIndex += 1
                if escape == False:
                    print("No other pieces on board. SORRY!")
                return False

    def moveHome(self, color, startCoord, movement, chosenPiece):
        #print("Work in progress")

        if movement == 4:
            movement *= -1

        if color == "Red":
            if self.redTeam.moveInHome(startCoord, movement) == True:

                destCoords = self.redTeam.pieces[chosenPiece - 1].coords

                if destCoords == pos.HOME:
                    print("Home!")
                    #exit(0)
                    return True

                if destCoords >= 0:

                    if self.matrix[destCoords].inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASRED
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASRED
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASRED
                        return True

                    else:
                        self.matrix[destCoords] = Inside.HASRED
                        return True
            else:
                print("Move not completed")
                return False

        if color == "Blue":
            if self.blueTeam.moveInHome(startCoord, movement) == True:

                destCoords = self.blueTeam.pieces[chosenPiece - 1].coords

                if destCoords == pos.HOME:
                    print("Home!")
                    #exit(0)
                    return True


                if destCoords >= 0:

                    if self.matrix[destCoords].inhabited == Inside.HASRED:
                        self.redTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASBLUE
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASBLUE
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASBLUE
                        return True

                    else:
                        self.matrix[destCoords] = Inside.HASBLUE
                        return True
            else:
                print("Move not completed")
                return False

        if color == "Yellow":
            if self.yellowTeam.moveInHome(startCoord, movement) == True:

                destCoords = self.yellowTeam.pieces[chosenPiece - 1].coords

                if destCoords == pos.HOME:
                    print("Home!")
                    #exit(0)
                    return True

                if destCoords >= 0:

                    if self.matrix[destCoords].inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASYELLOW
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASRED:
                        self.redTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASYELLOW
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASGREEN:
                        self.greenTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASYELLOW
                        return True

                    else:
                        self.matrix[destCoords] = Inside.HASYELLOW
                        return True
            else:
                print("Move not completed")
                return False

        if color == "Green":
            if self.greenTeam.moveInHome(startCoord, movement) == True:

                destCoords = self.greenTeam.pieces[chosenPiece - 1].coords

                if destCoords == pos.HOME:
                    print("Home!")
                    #exit(0)
                    return True


                if destCoords >= 0:

                    if self.matrix[destCoords].inhabited == Inside.HASBLUE:
                        self.blueTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASGREEN
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASYELLOW:
                        self.yellowTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASGREEN
                        return True

                    if self.matrix[destCoords].inhabited == Inside.HASRED:
                        self.redTeam.enterStart(destCoords)
                        self.matrix[destCoords].inhabited = Inside.HASGREEN
                        return True

                    else:
                        self.matrix[destCoords] = Inside.HASGREEN
                        return True
            else:
                print("Move not completed")
                return False

    def __str__(self):

        currIndex = 0

        for tile in self.matrix:
            if tile.inhabited == Inside.HASRED:
                print(currIndex, ": Red", )
            elif tile.inhabited == Inside.HASYELLOW:
                print(currIndex, ": Yellow", )
            elif tile.inhabited == Inside.HASBLUE:
                print(currIndex, ": Blue", )
            elif tile.inhabited == Inside.HASGREEN:
                print(currIndex, ": Green", )
            else:
                print(currIndex, ": ", )

            currIndex += 1

        print("Red Home: ", self.redTeam.homeStrip)
        print("Yellow Home: ", self.yellowTeam.homeStrip)
        print("Blue Home: ", self.blueTeam.homeStrip)
        print("Green Home: ", self.greenTeam.homeStrip)






inside = Inside.EMPTY

firstTile = Tile(inhabited=Inside.EMPTY, variation=Type.UNSAFE, position=20)
print(firstTile.item)
print(firstTile.inhabited)

firstBoard = Board()




