import pygame.font
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
light_blue = (64, 128, 255)
green = (0, 200, 64)
yellow = (255, 255, 0)
blue = (50, 170, 205)
pink = (255, 50, 255)
red = (255, 0, 0)
blue_green = (0, 255, 100)
maroon = (115, 0, 0)
lime = (230, 255, 101)
purple = (240, 0, 255)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (5, 100, 5)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
dandelion_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown = (200, 190, 140)
moon_glow = (235, 245, 255)

pi = 3.14159




ellipse(screen, forest_green, (70, 410, 100, 70))
polygon(screen, coffee_brown, [(80, 599), (130, 594), (105, 410), (92, 410)])
ellipse(screen, forest_green, (3, 380, 120, 80))
ellipse(screen, forest_green, (30, 320, 180, 120))
ellipse(screen, forest_green, (10, 280, 100, 70))
ellipse(screen, forest_green, (40, 240, 150, 100))
ellipse(screen, forest_green, (142, 276, 67, 44))
ellipse(screen, forest_green, (59, 140, 98, 135))
ellipse(screen, forest_green, (100, 190, 80, 105))
ellipse(screen, forest_green, (25, 175, 70, 140))
ellipse(screen, forest_green, (29, 160, 50, 40))
ellipse(screen, forest_green, (97, 120, 80, 60))
ellipse(screen, forest_green, (70, 90, 70, 100))
circle(screen, red, (69, 200), 7)
circle(screen, red, (139, 350), 7)
circle(screen, red, (159, 240), 7)










pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()