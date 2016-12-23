#demonstrating the gaussian distribution
from point import Point, RandomPoint

#for gaussian / normal distribution
p = None
#for uniform distribution
r = None


def setup():
    global p , r
    background(255)
    size(600, 400)
    p = Point(PVector(width/2, height/2))
    
    r = RandomPoint(PVector(width/2, height/2 + 100))

def draw():
    
    p.show()
    p.walk()
    
    r.show()
    r.randomWalk()