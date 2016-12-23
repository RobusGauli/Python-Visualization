class Sphere(object):
    
    def __init__(self, pos, vel, rad=40):
        self.pos = pos
        self.vel = vel
        self.rad = rad
        
    def show(self):
        noStroke()
        fill(0,255,0)
        pointLight(51, 102, 126, 35, 40, 36)
        directionalLight(51, 200, 126, -1, 0, 0)
        translate(self.pos.x, self.pos.y, 0)
        sphere(self.rad)
        
    def update(self):
        self.pos.add(self.vel)
        
    def makeBounce(self):
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x = self.vel.x * -1
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y = self.vel.y * -1
        