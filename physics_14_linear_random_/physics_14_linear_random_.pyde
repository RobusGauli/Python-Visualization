#linear randomness wihout using monte carlo
from random import randrange, choice
alist = []
for i in range(50):
    for j in range(i):
        alist.append(i-1)
w = None
l = [0 for i in range(52)]
print(alist)
def setup():
    global w
    size(600, 400)
    background(255)
    w = width/alist[-1]
def draw():
    ind = choice(alist)
    #this could be from o to 10
    l[ind] += 1
    for i, v in enumerate(l):
        rect(i * w, height, w, -v)
        
    
    
    