from enum import Enum
class pos(Enum):
    #define home and start positions
    HOME = -5
    START = -10

class Piece:
    #initialize Piece with color and number 1-4
    #return: nothing
    def __init__(self, color, number):
        self.color = color
        self.inStart = True
        self.inHome = False
        self.inHomeStrip = False
        self.coords = pos.START
        self.number = number
