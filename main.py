import pygame
import math
import Project_math
from Project_math import atan

pygame.init()
# make window :
screen_width = 800
screen_height= 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Target tracking turret")
clock = pygame.time.Clock()
x = screen_width/2
y = screen_height/2
#make turret:
turretImg  = pygame.image.load("turret.png").convert_alpha()
run = True
while run:

    #Display:
    screen.fill((255,255,255))
    #mouse :
    pos = pygame.mouse.get_pos()
    #get turret angle:
    x_d = pos[0] - x
    y_d = -(pos[1] - y)#(-)beacuse in pygame the y goes up the further you go down
    angle  = atan(x_d,y_d)


    #add turret:

    turret =pygame.transform.rotate(turretImg,angle - 90)
    turretRect = turret.get_rect(center=(x,y))
    screen.blit(turret,turretRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)


pygame.quit()