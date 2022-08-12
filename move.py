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