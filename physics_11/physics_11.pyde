#craeting a list of length 20 with value 0 at initial
#and increasing the value using the random fucntion


from random import randrange
alist = [0 for i in range(20)]

def setup():
    background(255)
    size(600, 300)
    
def draw():
    
    index = (randrange(0,20))
    alist[index] += 1
    
    noStroke()
    fill(175)
    
    w = width/len(alist)
    
    #random fucntion is not random after all , its vulnerable to security 
    #it shows uniform distribution accross the range of numbers
    #this randomness is call pseudo random
    for i, v in enumerate(alist):
        rect(w * index, height-v, w-5, v)
     