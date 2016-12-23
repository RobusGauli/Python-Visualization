def setup():
    
    size(600, 600)
    
def draw():
    background(255)
    #translate(width/2, height/2)
    center = PVector(width/2, height/2)
    mouse = PVector(mouseX, mouseY)
    print(mouse.x, mouse.y)
    #mouse.sub(center)
    #print(center.x, center.y)
    
    mouse.mult(0.5)
    line(0, 0, mouse.x, mouse.y)