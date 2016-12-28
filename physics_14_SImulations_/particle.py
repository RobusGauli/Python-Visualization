class Particle(object):
    
    def __init__(self, pos):
        self.pos = pos
        self.vel = PVector(random(15), random(15))
        self.acc = PVector(0, 0)
        
        
    def show(self):
        
        fill(0)
        ellipse(self.pos.x, self.pos.y, 4, 4)
        
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
        
    def applyForce(self, vector):
        self.acc.add(vector)
    
    def edge(self):
        if self.pos.x > width: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = width
        if self.pos.y > height: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = height
        
    def follow(self, vectors, cols, step):
        x = floor(self.pos.x/step)
        y = floor(self.pos.y/step)
        index = x + y * cols
        v = vectors[index]
        self.applyForce(v)
        