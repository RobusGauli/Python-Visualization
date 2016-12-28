cs = None
rs = None
inc = 0.03
zoff = 0

step_size = 30
def setup():
    global cs, rs
    size(600, 600, P2D)
    cs =floor( width / step_size)
    rs = floor(height / step_size)
    
def draw():
    global inc, zoff
    background(255)
    yoff = 0
    for row in range(rs):
        xoff = 0
        for col in range(cs):
            xoff += inc
            angle = noise(xoff, yoff, zoff) * TWO_PI
            v = PVector.fromAngle(angle)
            pushMatrix()
            translate(col * step_size, row * step_size)
            rotate(v.heading())
            line(0, 0, step_size,0)
            popMatrix()
            
            
            
        yoff += inc
        
    zoff += 0.03
        
    print(frameRate)