#perlin noise graph in 1 dimensional

xoff = 0
xinc = 0
def setup():
    size(500,300)
    
def draw():
    global xoff, xinc
    
    background(255)
    beginShape()
    xoff = xinc
    for i in range(width):
        xoff += 0.01
        x = i
        y = map(noise(xoff), 0, 1, 0, height)
        vertex(x, y)
        
    endShape()
    xinc += 0.02