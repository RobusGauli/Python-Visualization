class Food(object):
    cols = 600/20
    rows = cols
    def __init__(self):
        x = floor(random(self.cols)) * 20
        y = floor(random(self.rows)) * 20
        self.pos = PVector(x, y)
        
    def show(self):
        fill(255, 255,0)
        rect(self.pos.x, self.pos.y , 20, 20)
    
    
       