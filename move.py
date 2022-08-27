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

        # king movement
        pieces[(newpos[0] - 2, newpos[1])].coords = (newpos[0] + 1, newpos[1])

        pieces[(newpos[0] + 1, newpos[1])] = pieces[(newpos[0] - 2, newpos[1])]

        del pieces[(newpos[0] - 2, newpos[1])]

        pieces[initpos].nocastle = False # castling has occurred so no more castling

    # Kingside castling
    if pieces[initpos].name[1] == 'k' and (newpos[0] == initpos[0] + 2):

        # rook movement
        pieces[(newpos[0] + 1, newpos[1])].coords = (newpos[0] - 1, newpos[1])

        pieces[(newpos[0] - 1, newpos[1])] = pieces[(newpos[0] + 1, newpos[1])]

        del pieces[(newpos[0] + 1, newpos[1])]

        pieces[initpos].nocastle = False # castling has occurred so no more castling

    # getting total pts for either side, important for eval
    if pieces[initpos].name[0] == 'w':
        env.total += pieces[newpos].pt
    else:
        env.total += pieces[newpos].pt

    # moving piece
    pieces[initpos].coords = newpos
    pieces[newpos] = pieces[initpos]
    del pieces[initpos]

    # changing coordinates for white and black king in env
    if pieces[newpos].name == 'wk':
        env.wk = newpos
    if pieces[newpos].name == 'bk':
        env.bk = newpos

    # auto queen
    if pieces[newpos].name == 'wp' and newpos[1] == 0:
        pieces[newpos].name = 'wq'

    if pieces[newpos].name == 'bp' and newpos[1] == 7:
        pieces[newpos].name = 'bq'

    env.attackingSquaresW = []
    env.attackingSquaresB = []

    env, mate = updateAttackMoves(env, check)

    # to check if in check:
    
    if (env.bk in env.attackingSquaresW) or (env.wk in env.attackingSquaresB):

        print("in check")
        check = True
    else:
        check = False

    saveking = []

    # string of if statements that return all possible coordinates required from other pieces to stop mate
    # making sure it's only found once as if it's found twice it's double check and king has to move
    if env.attackingSquaresW.count(env.bk) == 1:
        for key in env.pieces:
            piece = env.pieces[key]

            if piece.name[0] == 'w':

                for coords in piece.attackMoves:
                    if coords == env.bk:
                        
                        saveking = findsaveking(piece, env)

        env, mate = updateAttackMoves(env, check, saveking, 'b')

    # string of if statements that return all possible coordinates required from other pieces to stop mate
    # making sure it's only found once as if it's found twice it's double check and king has to move
    if env.attackingSquaresB.count(env.wk) == 1:
        for key in env.pieces:
            piece = env.pieces[key]

            if piece.name[0] == 'b':

                for coords in piece.attackMoves:
                    if coords == env.wk:
                        
                        saveking = findsaveking(piece, env)

        env, mate = updateAttackMoves(env, check, saveking, 'w')

            


    return env, check, mate

# if piece that moved was obstructing a move for piece, it updates on this list using the piece movement functions
# PLEASE NOTE: The functions for Piece objects return circles, and since they aren't void functions, I used deez
# as a placeholder variable to receive 
def updateAttackMoves(env, check, saveking = [], color = ''):

    pmoves = []
    mate = False

    for key in env.pieces:

        env.pieces[key].pin = [0, 0, 0, 0] # resetting pin, allowing piece.findpinnedpieces() to see if the piece is still pinned

    # finding king moves first so all pieces will know if they're pinned
    filler = updateAttackMovesHelpFunc(env.pieces[env.wk], env, saveking)
    filler = updateAttackMovesHelpFunc(env.pieces[env.bk], env, saveking)

    for key in env.pieces:

        filler = updateAttackMovesHelpFunc(env.pieces[key], env, saveking)

        if check and env.pieces[key].name[0] == color: # only taking possible moves into account from pieces of color that's in check
            for coord in filler:
                pmoves.append(coord)

    if check and len(pmoves) == 0:
        print("Game Over")
        mate = True

    return env, mate

def updateAttackMovesHelpFunc(piece, env, saveking):

    deez = []

    piece.pieceobstr = []  # refreshing pieceobstr list so it has to search for all parameters again

    # if piece that moved was obstructing this piece, delete all attackingSquares that this piece was connected to
    # and reset them to see if there are any discovered checks

    piece.attackMoves = []

    if piece.name[1] == 'p':
        if piece.name[0] == 'w':
            piece.whitepawn(env.pieces, saveking)
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

        if piece.name[1] == 'k':
            piece.king(env.pieces)

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

        for coords in piece.attackMoves:
            if piece.name[0] == 'w':
                env.attackingSquaresW.append(coords)

            elif piece.name[0] == 'b':
                env.attackingSquaresB.append(coords)
    
    return env

# function that returns all possible coordinates that a piece could move to that would save the king from checkmate
def findsaveking(piece, env):
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

    # if a knight or pawn put the king in check
    elif piece.name[1] == 'n' or piece.name[1] == 'p':
        saveking = [piece.coords]

    return saveking

# function to see if a repetition is taking place
def repetition(fenstrings, env, repeat):

    # repeat is [<first time moves started repeating>, <current indices away from that initial repetition>]
    
    # if move is not being repeated
    if fenstrings.count(fenstrings[len(fenstrings) - 1]) == 1:
        return False, None

    elif (fenstrings.count(fenstrings[len(fenstrings) - 1]) == 3) and (repeat == [fenstrings.index(fenstrings[len(fenstrings) - 1]), repeat[1]]):
        print("Draw")
        return True, repeat

    elif fenstrings.count(fenstrings[len(fenstrings) - 1]) > 1:
        # this is the first piece of the repetition
        if repeat == None:
            return False, [fenstrings.index(fenstrings[len(fenstrings) - 1]), 0]

        elif repeat != None:

            # if still repeating
            if fenstrings[repeat[0] + repeat[1] + 1] == fenstrings[len(fenstrings) - 1]:
                return False, [repeat[0], repeat[1] + 1]

            # if no longer repeating
            else:
                return False, None

