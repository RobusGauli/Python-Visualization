#random walker
import math
from random import choice, randrange, randint

class Mover(object):
    
    def __init__(self, pos):
        self.pos = pos
        
    
    def show(self):
        point(self.pos.x, self.pos.y)
        
    def randomWalk(self):
        #create a random step
        randStep = randrange(0, 4)
        print(randStep)
        if randStep == 0:
            self.pos.x += 1
        elif randStep == 1:
            self.pos.x -= 1
        elif randStep == 2:
            self.pos.y += 1
        else:
            self.pos.y -= 1
            
mover = None        
def setup():
    size(600, 600)
    background(255)
    global mover
    mover = Mover(PVector(width/2, height/2))
                   
def draw():
    mover.show()
    mover.randomWalk()
    

    