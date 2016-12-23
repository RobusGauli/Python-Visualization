#a physics engine with OOPS
from ball import Ball

ball = None
def setup():
    #declare the ball as a global so that we can manipulate the global variable ball in the method scope
    global ball
    size(400, 600)
    pos = PVector(random(width), random(height))
    vel = PVector(5, -5)
    ball = Ball(pos=pos, vel=vel)
    
    
def draw():
    background(0)
    ## calling the method that shows the ellipse
    ball.show()
    ##apply the velocity 
    ball.update()
    #check to see if the ball toucshes the edge and apply the complementary velocity
    ball.makeBounce()
    
    
    
    