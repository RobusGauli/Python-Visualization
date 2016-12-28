class Snake(object):
    cols = floor(600/20)
    rows = cols
    
    def __init__(self, vel):
        x = floor(random(self.cols)) * 20
        y = floor(random(self.rows)) * 20
        self.pos = PVector(x, y)
        self.vel = PVector(20,0)
        
    def show(self):
        fill(255,0,255)
        rect(self.pos.x, self.pos.y, 20, 20)
        
    def eatFood(self, food):
        if self.pos.x == food.pos.x and self.pos.y == food.pos.y:
             x = floor(random(self.cols)) * 20
             y = floor(random(self.rows)) * 20
             food.pos = PVector(x, y)
             return True
        return False
            
    def update(self):
        self.pos.add(self.vel)
    
    def edge(self):
        if self.pos.x  > width: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = width
        
        if self.pos.y > height: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = height
    
    def changeDirection(self, key):
        if key=='w':
            if self.vel.y !=20:
                self.vel.x = 0
                self.vel.y = -20
        if key == 'a':
            if self.vel.x != 20:
                self.vel.x = -20
                self.vel.y = 0
        if key == 'd':
            if self.vel.x != -20:
                self.vel.x = 20
                self.vel.y = 0
        if key =='s':
            if self.vel.y != -20:
                self.vel.x = 0
                self.vel.y =20
                