class Ball(object):
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        
    def show(self):
        noStroke()
        fill(0, 205, 0, 97)
        ellipse(self.pos.x, self.pos.y, 80, 80)
        
    def update(self):
        self.pos.add(self.vel)
        
    def makeBounce(self):
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x = -self.vel.x
        
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y = -self.vel.y