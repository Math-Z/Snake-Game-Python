import pygame
import time
import random
from snakeLib.display import *
from snakeLib.character import *
from snakeLib.food import *

window()

def gameLoop():
    x = 400
    y = 300
    space = 10
    speed = 10

    gameOpen = True

    foodx = round(random.randrange(0, disHeight - 10) / 10) * 10
    foody = round(random.randrange(0, disWidth - 10) / 10) * 10

    snakeList = []
    snakeSize = 1

    while gameOpen:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOpen = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        if x >= disHeight or x < 0:
            gameOpen = False
        if y >= disWidth or y < 0:
            gameOpen = False

        dis.fill(bgColor)  
        foods(foodx, foody, space, space)
        pygame.display.update()

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeSize:
            del snakeList[0]

        snake(space, snakeList)
        score('Your score: ', snakeSize - 1, scoreColor)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, disHeight - 10) / 10) * 10
            foody = round(random.randrange(0, disWidth - 10) / 10) * 10
            snakeSize += 1

    dis.fill(bgColor)
    message('Game Over!', msgColor)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

gameLoop()