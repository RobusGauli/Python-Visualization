class Wall(object):
    
    def __init__(self):
        self.pos = PVector(width/2 , height-50)
        self.vel = PVector(0,0)
    
    def show(self):
        fill(255,255,0)
        rect(self.pos.x, self.pos.y, 110, 25)
        
    def move(self):
        if key == 'a': self.pos.add(PVector(-4, 0))
        if key == 'd': self.pos.add(PVector(4, 0))
    
    def isCollided(self, ball):
        distance = dist(self.pos.x, self.pos.y, ball.pos.x, ball.pos.y)
        if distance < 50 :
            print("hhhhasdhashdhasdhashd")
            return True
        return False
            