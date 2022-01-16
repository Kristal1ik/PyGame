import pygame


class Kristall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('game_imgs/Kristall1.png')
        self.image = pygame.transform.scale(img, (x * 2, y * 2))
        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect.x, self.rect.y