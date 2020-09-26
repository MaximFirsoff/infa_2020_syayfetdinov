import pygame
from pygame.draw import *
import pygame.font

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (255, 255, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

currentColor = (145, 254, 222)

rect(screen, (240, 240, 240), (20, 20, 560, 560))
circle(screen, YELLOW, (300, 280), 100)
circle(screen, BLACK, (300, 280), 100, 5)
circle(screen, RED, (340, 250), 18)
circle(screen, RED, (260, 253), 23)
circle(screen, BLACK, (340, 250), 10)
circle(screen, BLACK, (260, 253), 10)
circle(screen, BLACK, (340, 250), 19, 2)
circle(screen, BLACK, (260, 253), 24, 2)
circle(screen, BLACK, (340, 250), 10)
polygon(screen, BLACK, [(308, 230), (371, 203), (377, 206), (320, 239), (308, 230)])
polygon(screen, BLACK, [(295, 223), (220, 196), (218, 207), (290, 241), (295, 223)])
rect(screen, BLACK, (245, 318, 110, 21))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
