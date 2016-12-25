class Mover(object):
    
    def __init__(self):
        self.pos = PVector(width/2, height/2)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        
    def show(self):
        #fill(12, 80 )
        noStroke()
        
        ellipse(self.pos.x, self.pos.y, 50, 50)
    
    def update(self):
        #applying the acceratino to velocity causing velopcity t change over time
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        #resetting the acceleration to zero
        self.acc.mult(0)
        
    #force is a vector that causes a mass to accelerate
    def applyForce(self, vector):
        self.acc.add(vector)
        
    def edge(self):
        if self.pos.x > width or self.pos.x < 0: self.vel.x = self.vel.x * -1
        if self.pos.y > height or self.pos.y < 0: self.vel.y = self.vel.y * -1
        