#normalizing a vector
def setup():
    size(600, 600)
    
def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    #normalizing the vector #making it to unit vector
    mouse.normalize()
    #scaling it by 50 pixesls
    mouse.mult(50)
    #and then srawing the line
    line(0, 0, mouse.x, mouse.y)
    