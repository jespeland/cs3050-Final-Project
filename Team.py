from Piece import *

class Team:
    def __init__(self, color, start, end):
        self.color = color
        self.inHome = 0
        self.inStart = 4
        self.startCoords = start
        self.endCoords = end
        self.homeStrip = [None, None, None, None, None]
        self.pieces = [Piece(self.color, "1"), Piece(self.color, "2"), Piece(self.color, "3"), Piece(self.color, "4")]
    
    # Checks if there is a piece at a given coordinate
    # in: coords; the coordinates to be checked
    # out: true if piece is located at coords, false otherwise
    def pieceAt(self, coords):
        for piece in self.pieces:
            if piece.coords == coords:
                return True
        
        return False

    # Moves a piece on the outside of the board
    # in: start; the coordinates the piece is moved from
    #     end; the coordinates the piece is moved to
    # out: true if move was completed, false otherwise
    def move(self, start, end):
        for piece in self.pieces:
            if piece.coords == start:
                piece.coords = end
                return True
        
        return False
    
    # Moves the specified piece from the start zone onto the board
    # out: true if move completed, false otherwise
    def leaveStart(self, pieceIndex):
        piece = self.pieces[pieceIndex]
        if piece.inStart:
            piece.coords = self.startCoords
            piece.inStart = False
            self.inStart -= 1
            return True      

        return False

    # Moves a piece from the board into the start zone
    # in: coords; where the piece is being moved from
    # out: true if move completed, false otherwise
    def enterStart(self, coords):
        for piece in self.pieces:
            if piece.coords == coords:
                piece.coords = pos.START
                piece.inStart = True
                self.inStart += 1
                return True
        
        return False

    # Moves a piece from the outside ring to the safe zone
    # in: start; coords the piece is going to be moved from
    #     movement; how many spaces the piece is going to move
    # out: true if move completed, false otherwise
    def enterHomeStrip(self, start, movement):
        for piece in self.pieces:
            if piece.coords == start:
                endDist = self.endCoords - start
                if(endDist < 0):
                    endDist = endDist+60
                stripPos = movement - endDist - 1

                if stripPos == len(self.homeStrip):
                    piece.coords = pos.HOME
                    self.inHome += 1
                    return True

                if stripPos > len(self.homeStrip):
                    return False

                self.homeStrip[stripPos] = piece

                piece.coords = (-1 * stripPos) - 1
                piece.inHomeStrip = True
                return True
        
        return False
    
    # Moves a piece inside of the safe zone
    # in: start; place in the safe zone to move from
    #     movement; how many spaces the piece will move
    # out: true if move valid & completed, false otherwise
    def moveInHome(self, start, movement):
        for piece in self.pieces:
            if piece.coords == start:
                # movement into home
                if start - movement == pos['HOME'].value:
                    self.homeStrip[(-1 * start) - 1] = None
                    piece.coords = pos.HOME
                    piece.inHome = True
                    piece.inHomeStrip = False
                    self.inHome += 1
                    return True
                # movement out of safe zone
                elif start - movement >= 0:
                    boardPos = self.endCoords - (start - movement)
                    for piece in self.pieces:
                        if piece.coords == boardPos:
                            return False
                    
                    self.homeStrip[(-1 * start) - 1] = None
                    
                    
                    piece.coords = boardPos
                    piece.inHomeStrip = False
                    return True
                # movement within safe zone
                elif start - movement > pos['HOME'].value:
                    # target space not occupied
                    if (self.homeStrip[(-1 * start) - 1 + movement] == None):
                        self.homeStrip[(-1 * start) - 1] = None

                        piece.coords = start - movement
                        self.homeStrip[(-1 * (start - movement)) - 1] = piece
                        return True
                    # target space occupied
                    else:
                        return False

        return False