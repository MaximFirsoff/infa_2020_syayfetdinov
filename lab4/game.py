import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 0.2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

c = 0


def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 200)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    Vx = randint(0, 10)
    Vy = randint(0, 10)
    dt = 1



def click(event):
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if ((x1 - x) ^ 2 + (y1 - y) ^ 2) <= r ^ 2 is True:
                c = +1
                print(c)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
