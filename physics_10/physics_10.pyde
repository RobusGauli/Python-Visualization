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
        step_x = randint(-1, 1)
        step_y = randint(-1, 1)
        self.pos.x += step_x
        self.pos.y += step_y
        

            
mover = None        
def setup():
    size(600, 600)
    background(255)
    global mover
    mover = Mover(PVector(width/2, height/2))
                   
def draw():
    mover.show()
    mover.randomWalk()
    