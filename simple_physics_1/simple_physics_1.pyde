ball = None
def setup():
    global ball
    size(480, 400)
    pos = PVector(random(width), random(height))
    vel = PVector(0,3)
    accl = PVector(0.2, 0.1)
    ball = Ball(pos, vel, accl)
    
    
    
def draw():
    background(123);
    ball.show()
    ball.update()
    ball.bounce_back()

class Ball(object):
    
    def __init__(self, pos, vel, accl):
        self.pos = pos
        self.vel = vel
        self.accl = accl
    
    def show(self):
        noStroke()
        
        fill(0,12,10,90)
        
        ellipse(self.pos.x, self.pos.y, 80, 80)
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.accl)
        #self.accl.mult(0)
    
    def bounce_back(self):
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x = -self.vel.x
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y = - self.vel.y
            
        
    