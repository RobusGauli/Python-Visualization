#using the 3d spehere for the same physics
from sphere import Sphere
ball = None
def setup():
    global ball
    size(600, 500, P3D)
    pos = PVector(random(width), random(height))
    vel = PVector(3, -3)
    ball = Sphere(pos=pos, vel=vel)
def draw():
    background(0)
    ball.show()
    ball.update()
    ball.makeBounce()    
    
        