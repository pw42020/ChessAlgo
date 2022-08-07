

from re import S


class Piece:

    def __init__(self, piece, coords):
        self.name = piece

        self.dict = {'r': [5,'straight'], 'n': [3,'L'], 'b': [3,'diag'], 'q': [9,'all'], 'k': [5,'straight'],
                    }

        self.moved = False

        #self.pts = dict[piece.lower()][0]
        #self.dir = dict[piece.lower()][1]

        self.coords = coords
