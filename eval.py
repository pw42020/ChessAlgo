



class Eval:

    def __init__(self):
        self.fenstrings = []

    # function that returns fenstring of position
    def getfen(self,env):

        pieces = env.pieces

        fenstr = ''
        space = 0
        for row in range(8):
            if row != 0:
                fenstr += '/'
            for col in range(8):
                coords = (col, row)
                if coords in pieces:
                    
                    if space:
                        fenstr += str(space)
                    space = 0

                    if pieces[coords].name[0] == 'w':
                        fenstr += pieces[coords].name[1].upper()
                    else:
                        fenstr += pieces[coords].name[1]
                
                if coords not in pieces:
                    space += 1
                
            if space:
                fenstr += str(space)
                space = 0
            
            if env.movenum % 2 == 0:
                fenstr += ' w'
            elif env.movenum % 2 == 1:
                fenstr += ' b'
        
        self.fenstrings.append(fenstr)

        return fenstr
                
    def evalpos(self,env, pieces):
        pass