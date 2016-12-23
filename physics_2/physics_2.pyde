# a simple physics engine without OOP 

ball = None
pos = None
vel = None
    
def setup():
    global pos, vel
    size(500, 200)
    pos = PVector(random(width), random(height))
    #set the velocity vector
    vel = PVector(3,-3)

    global ball
    
def draw():
    background(0)
    global pos, vel
    noStroke()
        
    fill(255, 153, 0 , 100)
        
    ellipse(pos.x, pos.y, 80, 80)
    #apply the velocity vector to the current position
    pos.add(vel)
    
    #apply the bounce at the corner
    
    if pos.x > width or pos.x < 0:
        vel.x = -vel.x
    
    if pos.y > height or pos.y < 0:
        vel.y = -vel.y
    