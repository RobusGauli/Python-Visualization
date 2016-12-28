#lets make a pong gamme
from ball import Ball
from wall import Wall

ball = None
wall = None
def setup():
    global ball, wall
    size(400, 600)
    ball = Ball()
    wall = Wall()
def draw():
    background(0)
    ball.show()
    ball.update()
    ball.edge()
    
    wall.show()
    if wall.isCollided(ball):
        ball.pos.x = width/2
        ball.pos.y =height/2
    if keyPressed:
        wall.move()
    
    
    