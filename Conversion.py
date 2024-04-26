from Board import *

inside = Inside.EMPTY

firstTile = Tile(inhabited=Inside.EMPTY, variation=Type.UNSAFE, position=20)
print(firstTile.item)
print(firstTile.inhabited)

firstBoard = Board()

firstBoard.__str__()

choice = input("Move or quit")

while choice != "quit":


    firstBoard.turn(choice)

    firstBoard.__str__()

    choice = input("Move or quit")



