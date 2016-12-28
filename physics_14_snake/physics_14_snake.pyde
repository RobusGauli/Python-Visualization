from snake import Snake
from food import Food
from tail import Tail
cols = None
rows = None
step = 20
snake = None
food = None
tails = []
def setup():
    frameRate(18)
    #lets create a snake grid
    size(600, 600)
    global cols, rows, snake, food
    cols = width/step
    rows = height/step
    
    snake = Snake(PVector(3,0))
    food = Food()
    
    #lets create a grid
    
            
    
def draw():
    background(200)
    for y in range(rows):
        for x in range(cols):
            pushMatrix()
            translate(y*step, x*step)
            noFill()
            rect(0, 0, step, step)
            popMatrix()
    food.show()
         
    snake.show()
    snake.update()
    snake.edge()
    val = snake.eatFood(food)
    if val:
        tails.push(Tail(  
    if keyPressed:
        snake.changeDirection(key)        