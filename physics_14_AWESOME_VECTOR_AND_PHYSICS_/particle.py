from vector import Vector
class Particle(object):
    
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        
    def show(self):
        noStroke()
        ellipse(self.pos.x, self.pos.y, 30, 30)
    
    def update(self):
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel
        #each accelration value is a new value in a moment in time and the accumulation of all the forces summed up
        #therefore we need to multiply the vector by zero
        self.acc *= 0
        
    def applyForce(self, forceVector):
        self.acc += forceVector
    
    def edge(self):
        if self.pos.x > width: self.vel.x *= -1
        elif self.pos.x < 0: self.vel.x *= -1
        elif self.pos.y > height: self.vel.y *= -1
        elif self.pos.y < 0: self.vel.y *= -1
        