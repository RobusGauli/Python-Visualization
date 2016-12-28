from random import randrange, choice
class Ball(object):
    
    def __init__(self):
        self.pos = PVector(width/2, height/2)
        self.vel = PVector(0, choice([-3,3]))
        self.acc = PVector(0, 0)
        
    def show(self):
        fill(255)
        ellipse(self.pos.x, self.pos.y , 40, 40)
        
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    def applyForce(self, vector):
        self.acc.add(vector)
    
    def edge(self):
        if self.pos.x > width - 20: self.vel.x = self.vel.x * -1
        if self.pos.x < 20: self.vel.x = self.vel.x * -1
        
        if self.pos.y > height -20: self.vel.y = self.vel.y * -1
        if self.pos.y < 20: self.vel.y = self.vel.y * -1
        