def setup():
    size(600, 500)
    
def draw():
    background(255)
    
    mouse = PVector(mouseX, mouseY)
    origin = PVector(0, 0)
    #width of the rectangle accorind to the magnitude of mouse vector from origin
    mouse.mult(0.7)
    rect_x = mouse.mag()
    #this is will give the magnitude according the distance of mouse pointer 
    #from origin
    rect(0, 0, rect_x, 10)
    line(0, 0, mouse.x, mouse.y)