'''
Patrick Walsh
UMass Amherst Class of 2024
Building a Chess Machine Learning Algorithm
setup.py is to set up the game using pygame as I'll use tensorflow for ML
'''

from piece import Piece
import pygame

class GameEnv:

    def __init__(self, fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'):

        self.WIDTH, self.HEIGHT = 800, 800

        self.fen = fen

        self.pieces = {}

        self.movenum = 0

        self.initboard()

        self.circles = []

    # initializing board
    def initboard(self):
        pygame.init()
        
        self.ROWS, self.COLS = 8,8
        self.SQUARE_SIZE = self.WIDTH//self.COLS

        self.WHITE = (238, 238, 213)
        self.BLACK = (125, 148, 93)

        self.win = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Chess")

    
    # function to continuously draw checkerboard pattern and add any circles to show where piece selected can go
    def drawcubes(self):
        cubew = 100
        cubeh = 100

        self.win.fill(self.BLACK)

        for row in range(self.ROWS):

            for col in range(row % 2, self.ROWS, 2):

                pygame.draw.rect(self.win, self.WHITE, (row*self.SQUARE_SIZE, col*self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
        
        for circle in self.circles:

            img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\circle.png")          

            self.win.blit(img, (circle[0]*cubew, circle[1]*cubeh))
                


    # function to initialize pieces based off of fen string
    def initpiece(self):

        cubew = self.WIDTH/8
        cubeh = self.HEIGHT/8

        i = 0
        val = 0

        while (val != 64) and (i != len(self.fen)):

            char = self.fen[i]

            if char == '/':
                i += 1
            elif char.isdigit():
                for j in range(int(char)):
                    val += 1
                i += 1
            else:  # char is a character meaning this piece is supposed to be placed somewhere

                if char.isupper():
                    char = "w" + char.lower()
                else:
                    char = "b" + char

                piece = Piece(char, (val%8, val//8))

                self.pieces[(val%8, val//8)] = piece
                
                img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\"+char+".png")
                img = pygame.transform.scale(img, (cubew,cubeh))

                self.win.blit(img, ((val%8)*cubew, (val//8)*cubeh))

                i += 1
                val += 1

    # function to update pieces from their initial positions
    def updatepieces(self):

        cubew = self.WIDTH/8
        cubeh = self.HEIGHT/8

        for piece in self.pieces:

            p = self.pieces[piece]

            char = p.name

            img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\"+char+".png")
            img = pygame.transform.scale(img, (cubew,cubeh))

            self.win.blit(img, (p.coords[0]*cubew, p.coords[1]*cubeh))

    # set to move the pieces
    def move(self,coords):

        piece = self.pieces[coords]
                    
        
        # PAWN MOVEMENT
        if piece.name[1] == 'p':

            #MOVEMENT FOR BLACK PIECES
            if self.movenum % 2 == 1 and piece.name[0] == 'b': 

                # can move two pieces up if pawn hasn't moved
                if not piece.moved:
                    for i in range(2):
                        checkKey = (coords[0], coords[1] + i + 1)

                        if checkKey not in self.pieces:
                            self.circles.append(checkKey)

                if piece.moved:

                    checkKey = (coords[0], coords[1] + 1)

                    if checkKey not in self.pieces:
                            self.circles.append(checkKey)

                # diagonal motion
                if (coords[0] - 1, coords[1] + 1) in self.pieces and self.pieces[(coords[0] - 1, coords[1] + 1)].name[0] == 'w':
                    self.circles.append((coords[0] - 1, coords[1] + 1))

                if (coords[0] + 1, coords[1] + 1) in self.pieces and self.pieces[(coords[0] + 1, coords[1] + 1)].name[0] == 'w':
                    self.circles.append((coords[0] + 1, coords[1] + 1))

            #MOVEMENT FOR WHITE PIECES
            if self.movenum % 2 == 0 and piece.name[0] == 'w':
                if not piece.moved:
                    for i in range(2):
                        checkKey = (coords[0], coords[1] - i - 1)

                        if checkKey not in self.pieces:
                            self.circles.append(checkKey)

                if piece.moved:

                    checkKey = (coords[0], coords[1] - 1)

                    if checkKey not in self.pieces:
                            self.circles.append(checkKey)

                # diagonal motion
                if (coords[0] - 1, coords[1] - 1) in self.pieces and self.pieces[(coords[0] - 1, coords[1] - 1)].name[0] == 'b':
                    self.circles.append((coords[0] - 1, coords[1] - 1))

                if (coords[0] + 1, coords[1] - 1) in self.pieces and self.pieces[(coords[0] + 1, coords[1] - 1)].name[0] == 'b':
                    self.circles.append((coords[0] + 1, coords[1] - 1))
                
                
        # MOVEMENTS FOR ALL PIECES OTHER THAN PAWN

        '''
        ----3 Conditions for movement----
        1. If coordinate in front not in pieces dictionary
        2. If piece is in pieces dictionary but is enemy piece
        3. If piece is in pieces dictionary but is not enemy piece
        '''
                    


        # MOVEMENT FOR ROOK ** HAVE NOT IMPLEMENTED CASTLING YET **
        if piece.name[1] == 'r':
            
            # four for loops for each straight direction

            if (piece.name[0] == 'w' and self.movenum %2 == 0) or (piece.name[0] == 'b' and self.movenum % 2 == 1):

                self.circles = piece.straight(self.pieces)

        if piece.name[1] == 'b':
            
            # four for loops for each straight direction

            if (piece.name[0] == 'w' and self.movenum %2 == 0) or (piece.name[0] == 'b' and self.movenum % 2 == 1):

                self.circles = piece.diag(self.pieces)

        if piece.name[1] == 'q':
            
            # four for loops for each straight direction

            if (piece.name[0] == 'w' and self.movenum %2 == 0) or (piece.name[0] == 'b' and self.movenum % 2 == 1):

                self.circles = piece.straight(self.pieces) + piece.diag(self.pieces)

        if piece.name[1] == 'k':
            
            # four for loops for each straight direction

            if (piece.name[0] == 'w' and self.movenum %2 == 0) or (piece.name[0] == 'b' and self.movenum % 2 == 1):

                self.circles = piece.king(self.pieces)
        
        if piece.name[1] == 'n':
            
            # four for loops for each straight direction

            if (piece.name[0] == 'w' and self.movenum %2 == 0) or (piece.name[0] == 'b' and self.movenum % 2 == 1):

                self.circles = piece.l(self.pieces)


# after initpiece() initializes with self.fen, the pieces automate themselves and are refreshed remembering on where they
# used to be using their coordinates

if __name__ == "__main__":

    env = GameEnv()

    run = True
    clock = pygame.time.Clock()

    env.initpiece()

    initpos = None

    while run:

        clock.tick(60)
        env.drawcubes()

        env.updatepieces()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                x = int(pos[0]/100)
                y = int(pos[1]/100)

                if len(env.circles) != 0:

                    # taking piece
                    if (x,y) in env.circles:

                        env.pieces[initpos].coords = (x,y)
                        env.pieces[(x,y)] = env.pieces[initpos]

                        del env.pieces[initpos]

                        env.circles = []
                        env.movenum += 1

                        env.pieces[(x,y)].moved = True
                    
                    else: # IMPORTANT: ALLOWS PLAYER TO PICK A NEW PIECE
                        env.circles = []
                
                # choosing piece
                if len(env.circles) == 0:

                    if (x,y) in env.pieces:

                        initpos = (x,y)
                        env.move((x,y))

        
        pygame.display.update()
            
    pygame.quit()



        

