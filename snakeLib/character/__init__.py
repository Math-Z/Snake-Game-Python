import pygame
from snakeLib.display import *

charColor = (10, 120, 30)

def pythonSnake(x, y, width, height):
    pygame.draw.rect(dis, charColor, (x, y, width, height))

def snake(snakeSpace, snakeList):
    for x in snakeList:
        pythonSnake(x[0], x[1], snakeSpace, snakeSpace)