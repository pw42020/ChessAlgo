

class Piece:

    def __init__(self, piece, coords):
        self.name = piece

        self.moved = False

        self.coords = coords

        self.attackMoves = [] # attacking moves for the piece

        self.pieceobstr = [] # pieces that obstruct the pieces movement


    def straight(self, pieces, ROWS = 8, COLS = 8):

        circles = []

        # x direction
        for i in range(self.coords[0], COLS, 1):

            if (i + 1, self.coords[1]) not in pieces:
                circles.append((i + 1, self.coords[1]))
                self.attackMoves.append((i + 1, self.coords[1]))

            elif (i + 1, self.coords[1]) in pieces and pieces[(i + 1, self.coords[1])].name[0] != self.name[0]:
                circles.append((i + 1, self.coords[1]))
                self.attackMoves.append((i + 1, self.coords[1]))
                self.pieceobstr.append((i + 1, self.coords[1]))
                break

            elif (i + 1, self.coords[1]) in pieces and pieces[(i + 1, self.coords[1])].name[0] == self.name[0]:
                self.pieceobstr.append((i + 1, self.coords[1]))
                break

        for i in range(COLS - self.coords[0], COLS, 1):

            if (COLS - i - 1, self.coords[1]) not in pieces:
                circles.append((COLS - i - 1, self.coords[1]))
                self.attackMoves.append((COLS - i - 1, self.coords[1]))

            elif (COLS - i - 1, self.coords[1]) in pieces and pieces[(COLS - i - 1, self.coords[1])].name[0] != self.name[0]:
                circles.append((COLS - i - 1, self.coords[1]))
                self.attackMoves.append((COLS - i - 1, self.coords[1]))
                self.pieceobstr.append((COLS - i - 1, self.coords[1]))
                break

            elif (COLS - i - 1, self.coords[1]) in pieces and pieces[(COLS - i - 1, self.coords[1])].name[0] == self.name[0]:
                self.pieceobstr.append((COLS - i - 1, self.coords[1]))
                break


        # y direction
        for i in range(self.coords[1], ROWS, 1):

            if (self.coords[0], i + 1) not in pieces:
                circles.append((self.coords[0], i + 1))
                self.attackMoves.append((self.coords[0], i + 1))

            elif (self.coords[0], i + 1) in pieces and pieces[(self.coords[0], i + 1)].name[0] != self.name[0]:
                circles.append((self.coords[0], i + 1))
                self.attackMoves.append((self.coords[0], i + 1))
                self.pieceobstr.append((self.coords[0], i + 1))
                break

            elif (self.coords[0], i + 1) in pieces and pieces[(self.coords[0], i + 1)].name[0] == self.name[0]:
                self.pieceobstr.append((self.coords[0], i + 1))
                break

        for i in range(ROWS - self.coords[1],ROWS, 1):

            if (self.coords[0], ROWS - i - 1) not in pieces:
                circles.append((self.coords[0], ROWS - i - 1))
                self.attackMoves.append((self.coords[0], ROWS - i - 1))

            elif (self.coords[0], ROWS - i - 1) in pieces and pieces[(self.coords[0], ROWS - i - 1)].name[0] != self.name[0]:
                circles.append((self.coords[0], ROWS - i - 1))
                self.attackMoves.append((self.coords[0], ROWS - i - 1))
                self.pieceobstr.append((self.coords[0], ROWS - i - 1))
                break

            elif (self.coords[0], ROWS - i - 1) in pieces and pieces[(self.coords[0], ROWS - i - 1)].name[0] == self.name[0]:
                self.pieceobstr.append((self.coords[0], ROWS - i - 1))
                break

        return circles

    def diag(self,pieces, ROWS = 8, COLS = 8):
        circles = []

        i,j,k,l = 0,0,0,0

        ncoords = self.coords # values that won't show up
        
        # up to left
        while (ncoords[0] >= 0 and ncoords[1] >= 0):
            ncoords = (self.coords[0] - i - 1, self.coords[1] - i - 1)

            if ncoords not in pieces:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)
                
            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)
                self.pieceobstr.append(ncoords)
                break

            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                self.pieceobstr.append(ncoords)
                break
                
            i += 1

        ncoords = self.coords

        # down to left
        while (ncoords[0] >= 0 and ncoords[1] <= 7):
            ncoords = (self.coords[0] - j - 1, self.coords[1] + j + 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)

            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)
                self.pieceobstr.append(ncoords)
                break

            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                self.pieceobstr.append(ncoords)
                break
                
            j += 1

        ncoords = self.coords

        # down to right       
        while (ncoords[0] <= 7 and ncoords[1] <= 7):
            ncoords = (self.coords[0] + l + 1, self.coords[1] + l + 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)

            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)
                self.pieceobstr.append(ncoords)
                break

            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                self.pieceobstr.append(ncoords)
                break
                
            l += 1    

        ncoords = self.coords

        # up to right
        while (ncoords[0] <= 7 and ncoords[1] >= 0):
            ncoords = (self.coords[0] + k + 1, self.coords[1] - k - 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)

            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                self.attackMoves.append(ncoords)
                self.pieceobstr.append(ncoords)
                break

            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                self.pieceobstr.append(ncoords)
                break
                
            k += 1

        return circles

    def l(self,pieces):
        circles = []
        pmoves = [(-2, 1), (-1, 2), (2, -1), (1, -2),
            (1, 2), (-1, -2), (-2, -1), (2, 1)]

        for pos in pmoves:
            ncoords = (self.coords[0] + pos[0], self.coords[1] + pos[1])

            if (ncoords[0] >= 0 and ncoords[0] <= 7) and (ncoords[1] >= 0 and ncoords[1] <= 7):

                if ncoords not in pieces:
                    circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    circles.append(ncoords)
                    self.attackMoves.append(ncoords)
                    self.pieceobstr.append(ncoords)
                    break

                if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.pieceobstr.append(ncoords)
                    break

        return circles
    
    # King Movement: HAVE NOT YET IMPLEMENTED CASTLING AND CONCEPT THAT KING CANT MOVE INTO CHECK
    def king(self,pieces):

        circles = []

        pmoves = [(-1,0), (-1,-1), (-1,1),
            (0,1), (0,-1), (1,1), (1,0), (1,-1)] # possible moves

        for pos in pmoves:
            ncoords = (self.coords[0] + pos[0], self.coords[1] + pos[1])

            if (ncoords[0] >= 0 and ncoords[0] <= 7) and (ncoords[1] >= 0 and ncoords[1] <= 7):

                if ncoords not in pieces:
                    circles.append(ncoords)
                    self.attackMoves.append(ncoords)

                if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                    circles.append(ncoords)
                    self.attackMoves.append(ncoords)
                    self.pieceobstr.append(ncoords)
                    break

                if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                    self.pieceobstr.append(ncoords)
                    break
        
        # ALLOWING CASTLING BY APPENDING TO CIRCLES (move.py handles movements of pieces)
        if not self.moved:

            ncoords = (self.coords[0] + 1, self.coords[1])

            # checking kingside castling
            while ncoords not in pieces and ncoords[0] <= 7:

                ncoords = (ncoords[0] + 1, ncoords[1])


            if (pieces[ncoords].name == self.name[0] + 'r') and not pieces[ncoords].moved:
                circles.append((self.coords[0] + 2, self.coords[1]))

            ncoords = (self.coords[0] - 1, self.coords[1])

            # checking queenside castling
            while ncoords not in pieces and ncoords[0] >= 0:

                ncoords = (ncoords[0] - 1, ncoords[1])

            if (pieces[ncoords].name == self.name[0] + 'r') and not pieces[ncoords].moved:
                circles.append((self.coords[0] - 2, self.coords[1]))

        
        return circles
        