from mover import Mover
ball = None
wind = PVector(0.1, 0)
def setup():
    size(600, 400)
    global ball
    ball = Mover()
    
def draw():
    background(0)
    ball.show()
    ball.update()
    ball.edge()
    #lets give the gravity
    gravity = PVector(0, 0.2)
    ball.applyForce(gravity)
    
    
    #wind force
    wind = PVector(0.1, 0)
    
    if mousePressed:
        ball.applyForce(wind)
    print(frameRate)
       
        