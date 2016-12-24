from math import sin as si

class PerlinSin(object):
    
    def __init__(self, xinc, xdelta):
        self.xinc = xinc
        self.xdelta = xdelta
        
    def show(self):
        xoff = self.xinc
        beginShape()
        noFill()
        for i in range(width):
            x = i
            y = map(si(xoff), -1, 1, height/2, height/4) + map(noise(xoff), 0, 1, 0, 30)
            vertex(x, y+100)
            xoff += self.xdelta
        endShape()
    
            