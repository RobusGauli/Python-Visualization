from random import randrange, gauss
class Point(object):
    #this class shows the gaussian distribution/ normal distrubutin
    def __init__(self, pos):
        self.pos = pos
        
    def show(self):
        noStroke()
        fill(0, 40)
        ellipse(self.pos.x, self.pos.y, 18, 18)
    
    def walk(self):
        
        g_num = gauss(width/2, 60)
        self.pos.x = g_num
        
class RandomPoint(object):
    
    def __init__(self, pos):
        self.pos = pos
        
    def show(self):
        noStroke()
        fill(0, 20)
        ellipse(self.pos.x, self.pos.y, 40, 40)
        
    def randomWalk(self):
        r_step = randrange(0, width)
        self.pos.x = r_step