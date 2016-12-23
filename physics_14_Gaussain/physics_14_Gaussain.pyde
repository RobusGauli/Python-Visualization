
#a sloid representation on gaussain distribution
alist = [0 for i in range(400)]
from random import gauss, randrange
from math import floor

def setup():
    size(600, 400)
    background(255)
    
def draw():
    w = width/len(alist)
    gaussian_index = int(gauss(200, 25))
    alist[gaussian_index] += 1
    for i, v in enumerate(alist):
        rect(w*i, height, w-2, -v*3)    