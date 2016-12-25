#perline noise added to the circle
#x = rcos(theta)
#y = rsin(theta)
angle = 0
xoff = 1000
#drawing a circle
from math import sin, cos
def setup():
    size(600, 400)
    background(255)
    
def draw():
    global angle, xoff
    
    translate(width/2, height/2)
    
    rad = map(angle, 0, 360, 0, TWO_PI)
    x_pos = map(noise(xoff), 0, 1, 0.01, 0.09) *1050 * cos(rad)
    y_pos = map(noise(xoff), 0, 1, 0.01, 0.09) *1050 * sin(rad)
    fill(0, noise(xoff)*100)
    noStroke()
    ellipse(x_pos, y_pos, 2, 2)
    
    angle += 1
    
    if angle > 360:
        angle = 0
    xoff += 0.1