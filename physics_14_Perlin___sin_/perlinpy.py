class Perlin(object):
    
    def __init__(self, xinc, xdelta):
        self.xinc = xinc
        self.xdelta = xdelta
        
    def show(self):
        xoff = self.xinc
        beginShape()
        noFill()
        for i in range(width):
            x = i
            y = map(noise(xoff), 0, 1, 0, height)
            vertex(x, y)
            xoff += self.xdelta
        endShape()