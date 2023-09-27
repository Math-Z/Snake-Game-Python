import pygame
import random
from snakeLib.display import *

pig = (180, 80, 160)
lizard = (220, 110, 10)
rat = (110, 110, 110)
bird = (60, 150, 210)

foodColors = random.choice([pig, lizard, rat, bird])

def foods(x, y, width, height):
    pygame.draw.rect(dis, foodColors, (x, y, width, height))