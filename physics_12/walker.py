from random import randrange
class Walker(object):
    
    def __init__(self, pos):
        self.pos = pos
        
    def show(self):
        point(self.pos.x, self.pos.y)
        
    def walk(self):
        randomStep = randrange(2)
        if randomStep == 0:
            self.pos.y += 1
        else:
            self.pos.x += 1
        