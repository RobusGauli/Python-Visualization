from snake import Snake
class Tail(object):
    cols = floor(600/20)
    rows = cols
    
    def __init__(self, pos):
        self.pos = pos
        
    def show(self):
        fill(123,123,123)
        rect( self.pos.x, self.pos.y, 20, 20)
        