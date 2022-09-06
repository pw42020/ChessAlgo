'''
Patrick Walsh
UMass Amherst Class of 2024
Building a Chess Machine Learning Algorithm
setup.py is to set up the game using pygame as I'll use tensorflow for ML
'''

from piece import Piece
from eval import EvalPosition
import pygame
import move as move


class GameEnv:

    def __init__(self, fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w'):

        self.WIDTH, self.HEIGHT = 800, 800

        self.fen = fen

        self.pieces = {}

        self.attackingSquaresW = [] # squares that White is attacking (wr can take piece on d5 ex)
        self.attackingSquaresB = [] # squares that Black is attacking (br can take piece on d5 ex)

        self.movenum = 0

        self.initboard()

        self.circles = []

        self.moves = []

        self.wk, bk = (0,0), (0,0)

        self.total = 0 # total pieces for one side, positive means white has more material, vice versa for black

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

            if char == ' ':
                break

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

                if char == 'bk':
                    self.bk = (val%8, val//8)
                elif char == 'wk':
                    self.wk = (val%8, val//8)

                i += 1
                val += 1

        if self.fen[len(self.fen) - 1] == 'b':
            self.movenum = 1

    def initimage(self):
        for coord in self.pieces:
            img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\"+self.pieces[coord].name+".png")
            img = pygame.transform.scale(img, (100, 100))

            self.win.blit(img, coord)

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
        
        if self.movenum % 2 == 0 and piece.name[0] == 'w':
            self.circles = piece.circles

        elif self.movenum % 2 == 1 and piece.name[0] == 'b':
            self.circles = piece.circles
    
    # function that shows all squares white can capture in red, and all squares black can capture in green
    def showAttackMoves(self):

        cubew = self.WIDTH/8
        cubeh = self.HEIGHT/8

        uniquelist = []

        for coords in self.attackingSquaresW:

            if coords not in uniquelist:

                img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\attackmovew.png")

                self.win.blit(img, (coords[0]*cubew, coords[1]*cubeh))
            
                uniquelist.append(coords)
        
        uniquelist = []

        for coords in self.attackingSquaresB:

            if coords not in uniquelist:

                img = pygame.image.load("C:\\Users\\Ninja\\OneDrive\\Documents\\GitHub\\ChessAlgo\\Pieces\\attackmoveb.png")

                self.win.blit(img, (coords[0]*cubew, coords[1]*cubeh))

                uniquelist.append(coords)

# function to evaluate the position based on three factors listed below
def evalpos(env, pos, check, depth = 2):
    '''
    The three parts of evaluating a position
    part 1: How much material is one person up?
    part 2: How many spaces does each position attack?
    part 3: Do the best moves in the position capture material or take up more spaces?

    My goal with looking through the depth to see which move seems like the best move
    (i.e. which move loses the least amount of material)
    (with pieces I have all available moves in the position but to get more I'll have to
    make another env)
    '''

    eval = EvalPosition()

    p1 = env.total/3

    bestmove = None

    bestinit, bestmove = explorepositions(pos, check, depth)    


    return eval, bestinit, bestmove

def explorepositions(pos, check, depth):

    initpos = None
    bestmove = None

    if depth != 0:
        depth -= 1
        for key in env.pieces:
            piece = env.pieces[key]

            for coord in piece.circles:
                
                # setting up subEnvironment
                subEnv = GameEnv(fen = pos)
                subEnv.initpiece()
                subEnv.wk, subEnv.bk = env.wk, env.bk

                subEnv, mate = move.updateAttackMoves(subEnv, check)
                subEnv, check, mate = move.move(key, coord, subEnv, check)
                fen = eval.getfen(env)

                a, b = explorepositions(pos, check, depth)

        initpos, bestmove = versus(key, coord, initpos, bestmove)


                

    

    return initpos, bestmove


def versus(newinit, newmove, bestinit, bestmove):
    return bestinit, bestmove


            


# after initpiece() initializes with self.fen, the pieces automate themselves and are refreshed remembering on where they
# used to be using their coordinates

if __name__ == "__main__":

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    repeat = None
    draw = 0

    env = GameEnv()
    eval = EvalPosition()

    run = True
    clock = pygame.time.Clock()

    env.initpiece() # initializing board and pieces in environment
    env.initimage()

    env, mate = move.updateAttackMoves(env, False)

    initpos = None

    check = False

    mate = False

    while run and not draw and not mate:

        s = ''  # anything with s is only helping with PGN, not important to functionality of code

        clock.tick(60)
        env.drawcubes()

        env.updatepieces()

        #env.showAttackMoves()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                x = int(pos[0]/100)
                y = int(pos[1]/100)

                # if a piece has already been selected
                if len(env.circles) != 0:

                    # taking piece
                    if (x,y) in env.circles:
                        
                        if env.pieces[initpos].name[1] != 'p':
                            s += env.pieces[initpos].name[1].upper()

                        if (x,y) in env.pieces:
                            
                            if env.pieces[initpos].name[1] == 'p':
                                s += letters[initpos[0]]
                            s += 'x'

                        env, check, mate = move.move(initpos, (x,y), env, check)

                        s += letters[x] + str(8-y)

                        # castling fancy string stuff
                        if env.pieces[(x,y)].name[1] == 'k':
                            if initpos[0] - x == 2:
                                s = 'O-O-O'
                            if initpos[0] - x == -2:
                                s = 'O-O'

                        env.circles = []
                        env.movenum += 1

                        env.pieces[(x,y)].moved = True

                        if check:
                            s += '+'
                        env.moves.append(s)

                        fen = eval.getfen(env)
                        evalpos(env, fen, check)
                        draw, repeat = move.repetition(eval.fenstrings, env, repeat) # checking to see if moves are getting repeated
                        s = ''

                    
                    else: # IMPORTANT: ALLOWS PLAYER TO PICK A NEW PIECE
                        env.circles = []
                
                # choosing piece
                if len(env.circles) == 0:

                    if (x,y) in env.pieces:

                        initpos = (x,y)
                        env.move((x,y))

        pygame.display.update()
            
    pygame.quit()

    print('PGN of game:')

    for i, val in enumerate(env.moves):

        if i % 2 == 0:
            print(str((i//2) + 1)+'. ',end = '')

        print(val+' ', end = '')

        if i % 2 == 1:
            print()


        



        

