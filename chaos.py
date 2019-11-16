# credits to u/Ilya_agibor
# made some cosmetic changes and TypeError fixes

import pygame
from pygame.locals import *
import random


pygame.init()
screen = pygame.display.set_mode((700, 450))
pygame.display.set_caption('Chaos game')
x = 0
y = 0
x = random.randint(200, 500)
y = random.randint(100, 350)
working = True

while working:

    # pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    pygame.draw.circle(screen, (255, 0, 0), (500, 350), 3)  # C
    pygame.draw.circle(screen, (255, 0, 0), (200, 350), 3)  # B
    pygame.draw.circle(screen, (255, 0, 0), (350, 100), 3)  # A
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

    point = random.choice([1, 2, 3])
    point2 = random.choice([1, 2, 3])
    print(point)
    print(point2)
    if point == 1:
        x += 500
        x /= 2
        y += 350
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
    elif point == 2:
        x += 200
        x /= 2
        y += 350
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
    else:
        x += 350
        x /= 2
        y += 100
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

    if point2 == 1:
        x += 500
        x /= 2
        y += 350
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x,y), 1)
    elif point2 == 2:
        x += 200
        x /= 2
        y += 350
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
    elif point2 == 3:
        x += 350
        x /= 2
        y += 100
        y /= 2
        x = int(x)
        y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
    pygame.display.update()
