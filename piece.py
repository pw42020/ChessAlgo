'''
Piece.py is an object for every piece on the board. Knowing which spots a piece can move is handled by
the functions below. There's a different function for each type of piece, except for the Queen, which is handled
by concatenating the two lists made by straight() and diag()

All functions follow the same checks, as in:
First check is if the coordinate already has a piece there
-If not, add the piece to self.circles and attackMoves

-If it does, is the piece opposite colored? If so, add the piece to self.circles and attackMoves but stop parsing

-If it does already have a piece there and the piece is same colored, add nothing and stop parsing

What is saveking?
- When a king is found in check, move.py will find exactly how the king is in check (i.e. King on e1 is in check from bishop on c3)
- saveking is a list of all possible coordinates that will take the king out of check (taking the piece that put the king
in check or pinning itself between the king and the piece)
- if len(saveking) == 0 is if there is currently not a check so the piece can move anywhere it's not pinned
'''

class Piece:

    def __init__(self, piece, coords):
        self.name = piece

        self.moved = False

        self.coords = coords

        self.attackMoves = [] # attacking moves for the piece

        self.circles = []

        self.nocastle = True

        self.pin = [0, 0, 0, 0] # VERTICAL, HORIZONTAL, M = -1 PIN AND M = +1 PIN


    def straight(self, pieces, saveking = [], ROWS = 8, COLS = 8):

        self.circles = []

        if not self.pin[2] and not self.pin[3] and not self.pin[0]:

            # x direction
            for i in range(self.coords[0], COLS, 1):

                ncoords = (i+1, self.coords[1])

                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break

            for i in range(COLS - self.coords[0], COLS, 1):

                ncoords = (COLS - i - 1, self.coords[1])

                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break

        if not self.pin[2] and not self.pin[3] and not self.pin[1]:

            # y direction
            for i in range(self.coords[1], ROWS, 1):

                ncoords = (self.coords[0], i + 1)

                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break

            for i in range(ROWS - self.coords[1],ROWS, 1):

                ncoords = (self.coords[0], ROWS - i - 1)

                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break

    def diag(self,pieces, saveking = []):

        if self.name[1] == 'b':
            self.circles = []

        i,j,k,l = 0,0,0,0

        if not (self.pin[0] or self.pin[1] or self.pin[2]):

            ncoords = self.coords # values that won't show up
            
            # up to left
            while (ncoords[0] >= 0 and ncoords[1] >= 0):
                ncoords = (self.coords[0] - i - 1, self.coords[1] - i - 1)

                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break
                    
                i += 1

            ncoords = self.coords

            # down to right       
            while (ncoords[0] <= 7 and ncoords[1] <= 7):
                ncoords = (self.coords[0] + l + 1, self.coords[1] + l + 1)
                
                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break
                    
                l += 1    
            
        if not (self.pin[0] or self.pin[1] or self.pin[3]):

            ncoords = self.coords

            # up to right
            while (ncoords[0] <= 7 and ncoords[1] >= 0):
                ncoords = (self.coords[0] + k + 1, self.coords[1] - k - 1)
                
                if ncoords not in pieces:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break
                    
                k += 1

            ncoords = self.coords

            # down to left
            while (ncoords[0] >= 0 and ncoords[1] <= 7):
                ncoords = (self.coords[0] - j - 1, self.coords[1] + j + 1)
                
                if ncoords not in pieces:
                    if len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    else:
                        if ncoords in saveking:
                            self.circles.append(ncoords)

                elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    if len(saveking) != 0 and ncoords in saveking:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    elif len(saveking) == 0:
                        self.circles.append(ncoords)
                        self.attackMoves.append(ncoords)
                    break

                elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    break
                    
                j += 1

    def l(self, pieces, saveking = []):
        self.circles = []
        pmoves = [(-2, 1), (-1, 2), (2, -1), (1, -2),
            (1, 2), (-1, -2), (-2, -1), (2, 1)]

        if not (self.pin[0] or self.pin[1] or self.pin[2] or self.pin[3]):

            for pos in pmoves:
                ncoords = (self.coords[0] + pos[0], self.coords[1] + pos[1])

                if (ncoords[0] >= 0 and ncoords[0] <= 7) and (ncoords[1] >= 0 and ncoords[1] <= 7):

                    if ncoords not in pieces:
                        if len(saveking) != 0 and ncoords in saveking:
                            self.circles.append(ncoords)
                            self.attackMoves.append(ncoords)
                        elif len(saveking) == 0:
                            self.circles.append(ncoords)
                            self.attackMoves.append(ncoords)

                    elif ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                        if len(saveking) != 0 and ncoords in saveking:
                            self.circles.append(ncoords)
                            self.attackMoves.append(ncoords)
                        elif len(saveking) == 0:
                            self.circles.append(ncoords)
                            self.attackMoves.append(ncoords)
                        continue

                    elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                        self.attackMoves.append(ncoords)
                        continue
    
    # King Movement: HAVE NOT YET IMPLEMENTED CASTLING AND CONCEPT THAT KING CANT MOVE INTO CHECK
    def king(self, pieces, attacked = []):

        self.findpinnedpieces(pieces)

        self.circles = []

        pmoves = [(-1,0), (-1,-1), (-1,1),
            (0,1), (0,-1), (1,1), (1,0), (1,-1)] # possible moves

        for pos in pmoves:
            ncoords = (self.coords[0] + pos[0], self.coords[1] + pos[1])

            if (ncoords[0] >= 0 and ncoords[0] <= 7) and (ncoords[1] >= 0 and ncoords[1] <= 7):

                if ncoords not in pieces and ncoords not in attacked:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                if (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and ncoords not in attacked:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)
                    continue

                if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.attackMoves.append(ncoords)
                    continue
        
        # ALLOWING CASTLING BY APPENDING TO self.circles (move.py handles movements of pieces)
        if (not self.moved) and self.coords not in attacked and self.nocastle:

            ncoords = (self.coords[0] + 1, self.coords[1])

            # checking kingside castling
            while ncoords not in pieces and ncoords[0] <= 7:

                ncoords = (ncoords[0] + 1, ncoords[1])

            if (pieces[ncoords].name == self.name[0] + 'r') and (not pieces[ncoords].moved) and ((self.coords[0] + 2, self.coords[1]) not in attacked):
                self.circles.append((self.coords[0] + 2, self.coords[1]))

            ncoords = (self.coords[0] - 1, self.coords[1])

            # checking queenside castling
            while ncoords not in pieces and ncoords[0] >= 0:

                ncoords = (ncoords[0] - 1, ncoords[1])

            if (pieces[ncoords].name == self.name[0] + 'r') and not pieces[ncoords].moved and (self.coords[0] - 2, self.coords[1]) not in attacked:
                self.circles.append((self.coords[0] - 2, self.coords[1]))

    def blackpawn(self, pieces, saveking = []):
        self.circles = []

        if not (self.pin[1] or self.pin[2] or self.pin[3]):
            if not self.moved:
                for i in range(2):
                    checkKey = (self.coords[0], self.coords[1] + i + 1)

                    if len(saveking) == 0:
                        if checkKey not in pieces:
                            self.circles.append(checkKey)
                    else:
                        if checkKey in saveking and checkKey not in pieces:
                            self.circles.append(checkKey)

            if self.moved:

                checkKey = (self.coords[0], self.coords[1] + 1)

                if len(saveking) == 0:
                    if checkKey not in pieces:
                        self.circles.append(checkKey)
                else:
                    if checkKey in saveking and checkKey not in pieces:
                        self.circles.append(checkKey)

        if not (self.pin[0] or self.pin[1] or self.pin[2]):

            # diagonal motion
            ncoords = (self.coords[0] - 1, self.coords[1] + 1)
            if ncoords in pieces and pieces[ncoords].name[0] == 'w':
                if len(saveking) == 0:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                elif len(saveking) != 0 and ncoords in saveking:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

            elif ncoords not in pieces:
                self.attackMoves.append(ncoords)

        if not (self.pin[0] or self.pin[1] or self.pin[3]):

            ncoords = (self.coords[0] + 1, self.coords[1] + 1)
            if ncoords in pieces and pieces[ncoords].name[0] == 'w':
                if len(saveking) == 0:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                elif len(saveking) != 0 and ncoords in saveking:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

            elif ncoords not in pieces:
                self.attackMoves.append(ncoords)

    def whitepawn(self, pieces, saveking = []):

        self.circles = []

        if not (self.pin[1] or self.pin[2] or self.pin[3]):

            if not self.moved:
                for i in range(2):
                    checkKey = (self.coords[0], self.coords[1] - i - 1)

                    if len(saveking) == 0:
                        if checkKey not in pieces:
                            self.circles.append(checkKey)
                    else:
                        if checkKey in saveking and checkKey not in pieces:
                            self.circles.append(checkKey)

            if self.moved:

                checkKey = (self.coords[0], self.coords[1] - 1)

                if len(saveking) == 0:
                    if checkKey not in pieces:
                        self.circles.append(checkKey)
                else:
                    if checkKey in saveking and checkKey not in pieces:
                        self.circles.append(checkKey)

        if not (self.pin[0] or self.pin[1] or self.pin[3]):

            # diagonal motion
            ncoords = (self.coords[0] - 1, self.coords[1] - 1)
            if ncoords in pieces and pieces[ncoords].name[0] == 'b':
                if len(saveking) == 0:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                elif len(saveking) != 0 and ncoords in saveking:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

            elif ncoords not in pieces:
                self.attackMoves.append(ncoords)

        if not (self.pin[0] or self.pin[1] or self.pin[2]):

            ncoords = (self.coords[0] + 1, self.coords[1] - 1)
            if ncoords in pieces and pieces[ncoords].name[0] == 'b':
                if len(saveking) == 0:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                elif len(saveking) != 0 and ncoords in saveking:
                    self.circles.append(ncoords)
                    self.attackMoves.append(ncoords)

            elif ncoords not in pieces:
                self.attackMoves.append(ncoords)


    # function to find where pieces will be pinned on King
    def findpinnedpieces(self, pieces):

        piece = None
        ncoords = self.coords

        # all straight directions

        # vertical
        while ncoords[1] >= 0:
            ncoords = (ncoords[0], ncoords[1] - 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'r') and piece != None:
                pieces[piece].pin[0] = 1
                break

        
        ncoords = self.coords
        piece = None

        while ncoords[1] <= 0:
            ncoords = (ncoords[0], ncoords[1] + 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords
            
            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'r') and piece != None:
                pieces[piece].pin[0] = 1
                break
        
        ncoords = self.coords
        piece = None

        # horizontal
        while ncoords[0] >= 0:
            ncoords = (ncoords[0] - 1, ncoords[1])

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'r') and piece != None:
                pieces[piece].pin[1] = 1
                break

        ncoords = self.coords
        piece = None

        while ncoords[0] <= 7:
            ncoords = (ncoords[0] + 1, ncoords[1])

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'r') and piece != None:
                pieces[piece].pin[1] = 1
                break

        ncoords = self.coords
        piece = None

        # m = -1 diagonal
        while ncoords[0] >= 0 and ncoords[1] >= 0:
            ncoords = (ncoords[0] - 1, ncoords[1] - 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'b') and piece != None:
                pieces[piece].pin[2] = 1
                break

        ncoords = self.coords
        piece = None

        while ncoords[0] <= 7 and ncoords[1] <= 7:
            ncoords = (ncoords[0] + 1, ncoords[1] + 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'b') and piece != None:
                pieces[piece].pin[3] = 1
                break

        ncoords = self.coords
        piece = None

        # m = 1 diagonal
        while ncoords[0] >= 0 and ncoords[1] <= 7:
            ncoords = (ncoords[0] - 1, ncoords[1] + 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'b') and piece != None:
                pieces[piece].pin[3] = 1
                break

        ncoords = self.coords
        piece = None

        while ncoords[0] >= 0 and ncoords[1] <= 7:
            ncoords = (ncoords[0] - 1, ncoords[1] + 1)

            # piece ran into is same color
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece == None:
                piece = ncoords

            # two pieces in a row
            elif ncoords in pieces and pieces[ncoords].name[0] == self.name[0] and piece != None:
                break

            # if there is a direct pin from queen or rook
            elif (ncoords in pieces and pieces[ncoords].name[0] != self.name[0]) and (pieces[ncoords].name[1] == 'q' or pieces[ncoords].name[1] == 'b') and piece != None:
                pieces[piece].pin[2] = 1
                break



