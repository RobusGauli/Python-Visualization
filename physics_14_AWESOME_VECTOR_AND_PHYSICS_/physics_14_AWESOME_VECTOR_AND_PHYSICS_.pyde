#lets make a physics engine for the particle with the motion 
#interplated with the perlin noise
from particle import Particle
from vector import Vector
import vector
import math

particle = None

def setup():
    size(800, 600)
    global particle
    pos = Vector(width/2, height/2)
    
    particle = Particle(pos)
    

    
    
    
def draw():
    background(0)
    particle.show()
    particle.update()
    particle.edge()
    #create a gravity force vector
    
    gravity = Vector(0.0, 0.1)
    particle.applyForce(gravity)
    
    #create a wind force
    if mousePressed:
        angle = math.pi /6
        #creagine the unitVector from the angle
        unitVec = Vector.fromAngle(angle)
        
        particle.applyForce(unitVec)
        