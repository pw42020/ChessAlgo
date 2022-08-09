

class Piece:

    def __init__(self, piece, coords):
        self.name = piece

        self.moved = False

        self.coords = coords


    def straight(self, pieces, ROWS = 8, COLS = 8):

        circles = []

        # x direction
        for i in range(self.coords[0], COLS, 1):

            if (i + 1, self.coords[1]) not in pieces:
                circles.append((i + 1, self.coords[1]))

            elif (i + 1, self.coords[1]) in pieces and pieces[(i + 1, self.coords[1])].name[0] != self.name[0]:
                circles.append((+ i + 1, self.coords[1]))
                break

            elif (i + 1, self.coords[1]) in pieces and pieces[(i + 1, self.coords[1])].name[0] == self.name[0]:
                break

        for i in range(COLS - self.coords[0], COLS, 1):

            if (COLS - i - 1, self.coords[1]) not in pieces:
                circles.append((COLS - i - 1, self.coords[1]))

            elif (COLS - i - 1, self.coords[1]) in pieces and pieces[(COLS - i - 1, self.coords[1])].name[0] != self.name[0]:
                circles.append((COLS - i - 1, self.coords[1]))
                break

            elif (COLS - i - 1, self.coords[1]) in pieces and pieces[(COLS - i - 1, self.coords[1])].name[0] == self.name[0]:
                break


        # y direction
        for i in range(self.coords[1], ROWS, 1):

            if (self.coords[0], i + 1) not in pieces:
                circles.append((self.coords[0], i + 1))

            elif (self.coords[0], i + 1) in pieces and pieces[(self.coords[0], i + 1)].name[0] != self.name[0]:
                circles.append((self.coords[0], i + 1))
                break

            elif (self.coords[0], i + 1) in pieces and pieces[(self.coords[0], i + 1)].name[0] == self.name[0]:
                break

        for i in range(ROWS - self.coords[1],ROWS, 1):


            if (self.coords[0], ROWS - i - 1) not in pieces:
                circles.append((self.coords[0], ROWS - i - 1))

            elif (self.coords[0], ROWS - i - 1) in pieces and pieces[(self.coords[0], ROWS - i - 1)].name[0] != self.name[0]:
                circles.append((self.coords[0], ROWS - i - 1))
                break

            elif (self.coords[0], ROWS - i - 1) in pieces and pieces[(self.coords[0], ROWS - i - 1)].name[0] == self.name[0]:
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
            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                break
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                break
                
            i += 1

        ncoords = self.coords

        # down to left
        while (ncoords[0] >= 0 and ncoords[1] <= 7):
            ncoords = (self.coords[0] - j - 1, self.coords[1] + j + 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                break
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                break
                
            j += 1

        ncoords = self.coords

        # down to right       
        while (ncoords[0] <= 7 and ncoords[1] <= 7):
            ncoords = (self.coords[0] + l + 1, self.coords[1] + l + 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                break
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                break
                
            l += 1    

        ncoords = self.coords

        # up to right
        while (ncoords[0] <= 7 and ncoords[1] >= 0):
            ncoords = (self.coords[0] + k + 1, self.coords[1] - k - 1)
            
            if ncoords not in pieces:
                circles.append(ncoords)
            if ncoords in pieces and pieces[ncoords].name[0] != self.name[0]:
                circles.append(ncoords)
                break
            if ncoords in pieces and pieces[ncoords].name[0] == self.name[0]:
                break
                
            k += 1

        return circles

    def pawn(self,pieces):
        pass

    def L(self,pieces):
        pass

    def king(self,pieces):
        pass