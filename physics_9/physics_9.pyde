#random walker
import math
from random import choice, randrange, randint

x = None
y = None
cases = [i for i in range(4)]

def setup():
    global x, y
    size(600, 600)
    #declararing background here will make sure the point(walker) will leave the trace
    background(255)
    x = width/2
    y = height/2
def draw():
    global x, y
    rand = randrange(0,4)
    print(rand)
    if rand == 0:
        x += 1
    elif rand ==1:
        x -= 1
    elif rand == 2:
        y += 1
    else:
        y -= 1
    #now the point will move radomly according to the random value
    point(x, y)
    

    