import pygame

disHeight = 800
disWidth = 600
dis = pygame.display.set_mode((disHeight, disWidth))
bgColor = (250, 178, 96)

def window():
    pygame.init()
    dis
    dis.fill(bgColor)
    pygame.display.set_caption('Snake Game')

msgColor = (255, 0, 0)

def message(msg, color):
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render(msg, True, color)
    textRect = text.get_rect()
    textRect.center = (disHeight / 2, disWidth / 2)
    dis.blit(text, textRect)

scoreColor = (20, 20, 230)

def score(msg, score, color):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render(msg + str(score), True, color)
    textRect = text.get_rect()
    textRect.center = (disHeight / 2, disWidth / 12)
    dis.blit(text, textRect)