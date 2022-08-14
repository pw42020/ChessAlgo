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

    return env, check