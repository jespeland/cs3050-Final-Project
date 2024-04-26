
from enum import Enum

from Deck import *

class Type(Enum):
    START = "Start"
    UNSAFE = "Unsafe"
    SAFE = "Safe"
    HOME = "Home"


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

    def acceptPiece(piece):


    def exitPiece(piece):


    def __str__(self):
        return self.item

class Board:

    matrix = [Tile(inhabited=Inside.EMPTY, variation=Type.UNSAFE, position=i) for i in range(64)]
    startBlue = [Time(inhabited=Inside.HASBLUE, variation=Type.START, position=i) for i in range(4)]
    startRed = [Tile(inhabited=Inside.HASRED, variation=Type.START, position=i) for i in range(4)]
    startYellow = [Tile(inhabited=Inside.HASYELLOW, variation=Type.START, position=i) for i in range(4)]
    startGreen = [Time(inhabited=Inside.HASGREEN, variation=Type.START, position=i) for i in range(4)]


    theDeck = Deck()




inside = Inside.EMPTY

firstTile = Tile(inhabited=Inside.EMPTY, variation=Type.UNSAFE, position=20)
print(firstTile.item)
print(firstTile.inhabited)

firstBoard = Board()


