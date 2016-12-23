#Create a random walker that has a tendency to 
#move down and to the right. (We’ll see the solution to this in the next section.)
from walker import Walker

walker = None
def setup():
    size(600, 400)
    background(255)
    #creating the walker object
    global walker
    pos = PVector(width/2, height/2)
    walker = Walker(pos)
    
def draw():
    walker.show()
    walker.walk()
    