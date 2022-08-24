'''
move.py handles all moving of the pieces and the refreshing of attackSquares necessary after every move
It moves the pieces for castling but checking if the piece is available to castle is handled in piece.py
It will check available moves for other pieces as well by seeing if the King is in check and how to get them out of check
-Note: This is made BEFORE I implement checking functionality. I may have to change some functionality between this class
    and piece.py to get everything to work together.
'''



from tkinter.tix import CheckList
from piece import Piece

# function that will handle all moving
def move(initpos, newpos, env, check):

    pieces = env.pieces


    # CASTLING

    # Queenside castling
    if pieces[initpos].name[1] == 'k' and (newpos[0] == initpos[0] - 2):

        pieces[(newpos[0] - 2, newpos[1])].coords = (newpos[0] + 1, newpos[1])

        pieces[(newpos[0] + 1, newpos[1])] = pieces[(newpos[0] - 2, newpos[1])]

        del pieces[(newpos[0] - 2, newpos[1])]

    # Kingside castling
    if pieces[initpos].name[1] == 'k' and (newpos[0] == initpos[0] + 2):

        pieces[(newpos[0] + 1, newpos[1])].coords = (newpos[0] - 1, newpos[1])

        pieces[(newpos[0] - 1, newpos[1])] = pieces[(newpos[0] + 1, newpos[1])]

        del pieces[(newpos[0] + 1, newpos[1])]

    pieces[initpos].coords = newpos
    pieces[newpos] = pieces[initpos]
    del pieces[initpos]

    env.attackingSquaresW = []
    env.attackingSquaresB = []

    env = updateAttackMoves(env, check)

    # to check if in check:
    
    if (env.bk in env.attackingSquaresW) or (env.wk in env.attackingSquaresB):

        print("in check")
        check = True
    else:
        check = False

    saveking = []

    # string of if statements that return all possible coordinates required from other pieces to stop mate
    if (env.bk in env.attackingSquaresW):
        for key in env.pieces:
            piece = env.pieces[key]

            if piece.name[0] == 'w':

                for coords in piece.attackMoves:
                    if coords == env.bk:
                        # if a rook put the king in check
                        if piece.name[1] == 'r':
                            if env.bk[0] == piece.coords[0]:
                                if env.bk[1] > piece.coords[1]:
                                    saveking = [(env.bk[0], piece.coords[1] + i) for i in range(env.bk[1] - piece.coords[1])]
                                else:
                                    saveking = [(env.bk[0], env.bk[1] - i - 1) for i in range(piece.coords[1] - env.bk[1])]
                            elif env.bk[1] == piece.coords[1]:
                                if env.bk[0] > piece.coords[0]:
                                    saveking = [(env.bk[0] + i, piece.coords[1]) for i in range(env.bk[0] - piece.coords[0])]
                                else:
                                    saveking = [(env.bk[0] - i - 1, env.bk[1]) for i in range(piece.coords[0] - env.bk[0])]
                        # if a bishop put the king in check
                        elif piece.name[1] == 'b':
                            m = (env.bk[1] - piece.coords[1])/(env.bk[0] - piece.coords[0]) # slope of line

                            if m == -1:
                                if env.bk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] - i) for i in range(env.bk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] + i) for i in range(piece.coords[0] - env.wk[0])]
                            elif m == 1:
                                if env.bk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] + i) for i in range(env.bk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] - i) for i in range(piece.coords[0] - env.wk[0])]

                        # if a queen put the king in check
                        elif piece.name[1] == 'q':
                            m = (env.bk[1] - piece.coords[1])/(env.bk[0] - piece.coords[0]) # slope of line

                            if m == -1:
                                if env.bk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] - i) for i in range(env.bk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] + i) for i in range(piece.coords[0] - env.bk[0])]
                            elif m == 1:
                                if env.bk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] + i) for i in range(env.bk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] - i) for i in range(piece.coords[0] - env.bk[0])]
                            else:
                                if env.bk[0] == piece.coords[0]:
                                    if env.bk[1] > piece.coords[1]:
                                        saveking = [(env.bk[0], piece.coords[1] + i) for i in range(env.bk[1] - piece.coords[1])]
                                    else:
                                        saveking = [(env.bk[0], env.bk[1] - i - 1) for i in range(piece.coords[1] - env.bk[1])]
                                elif env.bk[1] == piece.coords[1]:
                                    if env.bk[0] > piece.coords[0]:
                                        saveking = [(env.bk[0] + i, piece.coords[1]) for i in range(env.bk[0] - piece.coords[0])]
                                    else:
                                        saveking = [(env.bk[0] - i - 1, env.bk[1]) for i in range(piece.coords[0] - env.bk[0])]

                        # if a knight put the king in check
                        elif piece.name[1] == 'n' or piece.name[1] == 'p':
                            saveking = [piece.coords]

        env = updateAttackMoves(env, check, saveking, 'b')

    # string of if statements that return all possible coordinates required from other pieces to stop mate
    if (env.wk in env.attackingSquaresB):
        for key in env.pieces:
            piece = env.pieces[key]

            if piece.name[0] == 'b':

                for coords in piece.attackMoves:
                    if coords == env.wk:
                        # if a rook put the king in check
                        if piece.name[1] == 'r':
                            if env.wk[0] == piece.coords[0]:
                                if env.wk[1] > piece.coords[1]:
                                    saveking = [(env.wk[0], piece.coords[1] + i) for i in range(env.wk[1] - piece.coords[1])]
                                else:
                                    saveking = [(env.wk[0], env.wk[1] - i - 1) for i in range(piece.coords[1] - env.wk[1])]
                            elif env.wk[1] == piece.coords[1]:
                                if env.wk[0] > piece.coords[0]:
                                    saveking = [(env.wk[0] + i, piece.coords[1]) for i in range(env.wk[0] - piece.coords[0])]
                                else:
                                    saveking = [(env.wk[0] - i - 1, env.wk[1]) for i in range(piece.coords[0] - env.wk[0])]
                        # if a bishop put the king in check
                        elif piece.name[1] == 'b':
                            m = (env.wk[1] - piece.coords[1])/(env.wk[0] - piece.coords[0]) # slope of line

                            if m == -1:
                                if env.wk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] - i) for i in range(piece.coords[0] - env.wk[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] + i) for i in range(env.wk[0] - piece.coords[0])]
                            elif m == 1:
                                if env.wk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] + i) for i in range(piece.coords[0] - env.wk[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] - i) for i in range(env.wk[0] - piece.coords[0])]

                        # if a queen put the king in check
                        elif piece.name[1] == 'q':
                            m = (env.wk[1] - piece.coords[1])/(env.wk[0] - piece.coords[0]) # slope of line

                            if m == -1:
                                if env.wk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] - i) for i in range(env.wk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] + i) for i in range(piece.coords[0] - env.wk[0])]
                            elif m == 1:
                                if env.wk[0] > piece.coords[0]:
                                    saveking = [(piece.coords[0] + i, piece.coords[1] + i) for i in range(env.wk[0] - piece.coords[0])]
                                else:
                                    saveking = [(piece.coords[0] - i, piece.coords[1] - i) for i in range(piece.coords[0] - env.wk[0])]
                            else:
                                if env.wk[0] == piece.coords[0]:
                                    if env.wk[1] > piece.coords[1]:
                                        saveking = [(env.wk[0], piece.coords[1] + i) for i in range(env.wk[1] - piece.coords[1])]
                                    else:
                                        saveking = [(env.wk[0], env.wk[1] - i - 1) for i in range(piece.coords[1] - env.wk[1])]
                                elif env.wk[1] == piece.coords[1]:
                                    if env.wk[0] > piece.coords[0]:
                                        saveking = [(env.wk[0] + i, piece.coords[1]) for i in range(env.wk[0] - piece.coords[0])]
                                    else:
                                        saveking = [(env.wk[0] - i - 1, env.wk[1]) for i in range(piece.coords[0] - env.wk[0])]

                        # if a knight put the king in check
                        elif piece.name[1] == 'n' or piece.name[1] == 'p':
                            saveking = [piece.coords]

        env = updateAttackMoves(env, check, saveking, 'w')

            


    return env, check

# if piece that moved was obstructing a move for piece, it updates on this list using the piece movement functions
# PLEASE NOTE: The functions for Piece objects return circles, and since they aren't void functions, I used deez
# as a placeholder variable to receive 
def updateAttackMoves(env, check, saveking = [], color = ''):

    pmoves = []

    for key in env.pieces:
        filler = updateAttackMovesHelpFunc(env.pieces[key], env, saveking)

        if check and env.pieces[key].name[0] == color: # only taking possible moves into account from pieces of color that's in check
            for coord in filler:
                pmoves.append(coord)

    if check and len(pmoves) == 0:
        print("Game Over")

    return env

def updateAttackMovesHelpFunc(piece, env, saveking):

    deez = []

    piece.pieceobstr = []  # refreshing pieceobstr list so it has to search for all parameters again

    # if piece that moved was obstructing this piece, delete all attackingSquares that this piece was connected to
    # and reset them to see if there are any discovered checks

    piece.attackMoves = []

    if piece.name[1] == 'p':
        if piece.name[0] == 'w':
            piece.whitepawn(env.pieces, saveking)
            print(saveking)
        elif piece.name[0] == 'b':
            piece.blackpawn(env.pieces, saveking)

    if piece.name[1] == 'r':
        piece.straight(env.pieces, saveking)

    if piece.name[1] == 'b':
        piece.diag(env.pieces, saveking)

    if piece.name[1] == 'n':
        piece.l(env.pieces, saveking)

    if piece.name[1] == 'q':

        piece.straight(env.pieces, saveking)
        piece.diag(env.pieces, saveking)

    if piece.name[1] == 'k':
        if piece.name[0] == 'w':
            piece.king(env.pieces, env.attackingSquaresB)
        if piece.name[0] == 'b':
            piece.king(env.pieces, env.attackingSquaresW)

    for coords in piece.attackMoves:
        if piece.name[0] == 'w':
            env.attackingSquaresW.append(coords)

        elif piece.name[0] == 'b':
            env.attackingSquaresB.append(coords)

    for coord in piece.circles:
        deez.append(coord)
    
    return deez
    

# initializes all attackMove and pieceobstr lists to not run into any funny business before a piece has moved
def initAttackMoves(env):
    for key in env.pieces:
        deez = [] # even though deez isn't used this is to keep it from overflowing after 100+ moves
        piece = env.pieces[key]

        if piece.name[1] == 'p':
            if piece.name[0] == 'w':
                piece.whitepawn(env.pieces)

            if piece.name[0] == 'b':
                piece.blackpawn(env.pieces)

        if piece.name[1] == 'r':
            piece.straight(env.pieces)

        if piece.name[1] == 'b':
            piece.diag(env.pieces)

        if piece.name[1] == 'n':
            piece.l(env.pieces)

        if piece.name[1] == 'q':

            piece.straight(env.pieces)
            piece.diag(env.pieces)

        if piece.name[1] == 'k':
            piece.king(env.pieces)

        for coords in piece.attackMoves:
            if piece.name[0] == 'w':
                env.attackingSquaresW.append(coords)

            elif piece.name[0] == 'b':
                env.attackingSquaresB.append(coords)
    
    return env

