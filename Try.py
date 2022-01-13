import pygame
import sys
import random
import math

from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
particles = []
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            particles.append([[pygame.Rect(mx, my, 10, 10)]])
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for particle in particles:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 255, 255), particle[0][0])
        radians = math.atan2((particle[0][0].y - my), (particle[0][0].x - mx))
        dy1 = math.sin(radians)
        dx1 = math.cos(radians)
        particle[0][0].x -= dx1
        particle[0][0].y -= dy1

    pygame.display.update()
    clock.tick(60)