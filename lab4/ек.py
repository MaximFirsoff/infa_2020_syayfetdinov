import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 35
s_x = 1200
s_y = 600
screen = pygame.display.set_mode((s_x, s_y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

n = 0
c = 0
a = 0


def new_ball_1():
    '''creates a random ball in a random place
 '''
    global x_1, y_1, r_1, Vx_1, Vy_1, color_1
    x_1 = randint(100, 1100)
    y_1 = randint(100, 500)
    r_1 = randint(10, 100)
    Vx_1 = randint(0, 10)
    Vy_1 = randint(0, 10)
    color_1 = COLORS[randint(0, 5)]


def new_ball_2():
    '''creates a random ball in a random place
 '''
    global x_2, y_2, r_2, Vx_2, Vy_2, color_2
    x_2 = randint(100, 1100)
    y_2 = randint(100, 500)
    r_2 = randint(10, 100)
    Vx_2 = randint(0, 10)
    Vy_2 = randint(0, 10)
    color_2 = COLORS[randint(0, 5)]


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
            if ((x1 - x_1) ** 2 + (y1 - y_1) ** 2) <= r_1 ** 2:
                n += 1
                print(n)
                c = 0
            if ((x1 - x_2) ** 2 + (y1 - y_2) ** 2) <= r_2 ** 2:
                n += 1
                print(n)
                a = 0
    c += 1
    if c < 200:
        if c < 2:

            new_ball_1()
        else:
            if x_1 + r_1 > s_x:
                Vx_1 = -randint(0, 10)
                Vy_1 = randint(0, 10)
            elif x_1 - r_1 < 0:
                Vx_1 = randint(0, 10)
                Vy_1 = randint(0, 10)
            elif y_1 + r_1 > s_y:
                Vx_1 = randint(0, 10)
                Vy_1 = -randint(0, 10)
            elif y_1 - r_1 < 0:
                Vx_1 = randint(0, 10)
                Vy_1 = randint(0, 10)
            x_1 += Vx_1
            y_1 += Vy_1
            circle(screen, color_1, (x_1, y_1), r_1)
    else:
        c = 0

    a += 1
    if a < 200:
        if a < 2:
            new_ball_2()
        else:
            if x_2 + r_2 > s_x:
                Vx_2 = -randint(0, 10)
                Vy_2 = randint(0, 10)
            elif x_2 - r_2 < 0:
                Vx_2 = randint(0, 10)
                Vy_2 = randint(0, 10)
            elif y_2 + r_2 > s_y:
                Vx_2 = randint(0, 10)
                Vy_2 = -randint(0, 10)
            elif y_2 - r_2 < 0:
                Vx_2 = randint(0, 10)
                Vy_2 = randint(0, 10)
            x_2 += Vx_2
            y_2 += Vy_2
            circle(screen, color_2, (x_2, y_2), r_2)

    else:
        a = 0
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
