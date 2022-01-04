import os
import random

import pygame


class Pers(pygame.sprite.Sprite):
    image = pygame.image.load('game_imgs\pers.jpg')
    image = pygame.transform.scale(image, (100, 100))

    def __init__(self, group):
        super().__init__(group)
        self.image = Pers.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if args and args[0][pygame.K_s]:
            self.rect.top += 10
        if args and args[0][pygame.K_w]:
            self.rect.top -= 10
        if args and args[0][pygame.K_d]:
            self.rect.right += 10
        if args and args[0][pygame.K_a]:
            self.rect.right -= 10


