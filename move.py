'''
move.py handles all moving of the pieces and the refreshing of attackSquares necessary after every move
It moves the pieces for castling but checking if the piece is available to castle is handled in piece.py
It will check available moves for other pieces as well by seeing if the King is in check and how to get them out of check
-Note: This is made BEFORE I implement checking functionality. I may have to change some functionality between this class
    and piece.py to get everything to work together.
'''



from piece import Piece

# function that will handle all moving
def move(initpos, newpos, env, check):

    check = False

    pieces = env.pieces

    # to check if in check:
    





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

    env = updateAttackMoves(env, initpos, newpos)

    return env, check

# if piece that moved was obstructing a move for piece, it updates on this list using the piece movement functions
# PLEASE NOTE: The functions for Piece objects return circles, and since they aren't void functions, I used deez
# as a placeholder variable to receive 
def updateAttackMoves(env, initpos, newpos):

    updateAttackMovesHelpFunc(env.pieces[newpos],env, initpos)

    for key in env.pieces:
        deez = [] # even though deez isn't used this is to keep it from overflowing after 100+ moves
        piece = env.pieces[key]
        if initpos in piece.pieceobstr:

            
        
            updateAttackMovesHelpFunc(env.pieces[key], env, initpos)

    return env

def updateAttackMovesHelpFunc(piece, env, initpos):

    piece.pieceobstr = []  # refreshing pieceobstr list so it has to search for all parameters again

    # if piece that moved was obstructing this piece, delete all attackingSquares that this piece was connected to
    # and reset them to see if there are any discovered checks
    for coords in piece.attackMoves:
        if piece.name[0] == 'w':
            env.attackingSquaresW.remove(coords)
        if piece.name[0] == 'b':
            env.attackingSquaresB.remove(coords)

    piece.attackMoves = []

    if piece.name[1] == 'p':
        if initpos not in piece.attackMoves:
            piece.attackMoves.append(initpos)

    if piece.name[1] == 'r':
        deez = piece.straight(env.pieces)

    if piece.name[1] == 'b':
        deez = piece.diag(env.pieces)

    if piece.name[1] == 'n':
        deez = piece.l(env.pieces)

    if piece.name == 'q':
        deez = piece.straight(env.pieces) + piece.diag(env.pieces)

    if piece.name == 'k':
        deez = piece.king(env.pieces)

    for coords in piece.attackMoves:
        if piece.name[0] == 'w':
            env.attackingSquaresW.append(coords)

        elif piece.name[1] == 'b':
            env.attackingSquaresB.append(coords)
    

# initializes all attackMove and pieceobstr lists to not run into any funny business before a piece has moved
def initAttackMoves(env):
    for key in env.pieces:
        deez = [] # even though deez isn't used this is to keep it from overflowing after 100+ moves
        piece = env.pieces[key]

        if piece.name[1] == 'p':
            if piece.name[0] == 'w':
                piece.attackMoves = [(key[0] - 1 ,key[1] - 1), (key[0] + 1 ,key[1] - 1)]

            if piece.name[0] == 'b':
                piece.attackMoves = [(key[0] - 1 ,key[1] + 1), (key[0] + 1 ,key[1] + 1)]

        if piece.name[1] == 'r':
            deez = piece.straight(env.pieces)

        if piece.name[1] == 'b':
            deez = piece.diag(env.pieces)

        if piece.name[1] == 'n':
            deez = piece.l(env.pieces)

        if piece.name == 'q':
            deez = piece.straight(env.pieces) + piece.diag(env.pieces)

        if piece.name == 'k':
            deez = piece.king(env.pieces)

        for coords in piece.attackMoves:
            if piece.name[0] == 'w':
                env.attackingSquaresW.append(coords)

            elif piece.name[0] == 'b':
                env.attackingSquaresB.append(coords)

    print(env.attackingSquaresW)
    print()
    print(env.attackingSquaresB)

    return env

