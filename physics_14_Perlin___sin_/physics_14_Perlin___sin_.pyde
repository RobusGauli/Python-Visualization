#demonstaation of sine wave and perlin noise intermixed
from perlinpy import Perlin
from PerlinSin import PerlinSin
from sin import Sin
perlins = []

def setup():
    global perlin
    size(600, 400)
    perlinsin = PerlinSin(1000, 0.02)
    sin_wave = Sin(1000, 0.02)
    
    perlins.append(sin_wave)
    perlins.append(perlinsin)
    
def draw():
    background(255)
    for perlin in perlins:
        perlin.show()
        perlin.xinc += 0.02


    
    