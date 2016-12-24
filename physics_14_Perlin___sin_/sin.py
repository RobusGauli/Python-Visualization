from math import sin as si

class Sin(object):
    
    def __init__(self, xinc, xdelta):
        self.xinc = xinc
        self.xdelta = xdelta
        
    def show(self):
        
        xoff = self.xinc
        beginShape()
        noFill()
        for i in range(width):
            x = i
            y = map(si(xoff), -1, 1, height/2, height/4)
            vertex(x, y)
            xoff += self.xdelta
        endShape()
        
            