cols = None
rows = None

step = 60
#global zoff
zoff = 0

vectors = None
from particle import Particle
particles = None
def setup():
    
    global particles, vectors
    size(600, 600, P2D)
    global cols, rows
    cols = width/step
    rows = height/step
    particles = [Particle(PVector(random(width), random(height))) for i in range(4)]
    vectors = [None for i in range(cols*rows)]
    print(len(vectors))
def draw():
    global zoff, vectors
    zoff += 0.05
    background(255)
    yoff = 0
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            
            noFill()
            pushMatrix()
            xoff += 0.1
            translate(y* step, x * step)
            #create a vector 
            angle = noise(xoff, yoff, zoff) * TWO_PI
            v = PVector.fromAngle(angle)
            v.mult(0.2)
            rotate(v.heading())
            line(0, 0, step, 0)
            index = x + (y * cols) 
            vectors[index] = v
            
            popMatrix()
        yoff += 0.01
    for particle in particles:
        particle.show()
        particle.update()
        particle.edge()
        if not None in vectors:
            particle.follow(vectors, cols, 60)