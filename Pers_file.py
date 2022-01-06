import pygame


class Pers(pygame.sprite.Sprite):
    image = pygame.image.load('game_imgs\Charecter.png')
    image = pygame.transform.scale(image, (50, 90))
    # у персонажа изначальный размер = 100 * 60 пикселей

    def __init__(self, group):
        super().__init__(group)
        self.image = Pers.image
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 450

    def update(self):
        #Изменены клавиши управления, чтобы при работе не было конфликта с классом Arrow.
        #Теперь управление как в большинстве игр - WASD

        #Упращено
        dx = 0
        dy = 0
        args = pygame.key.get_pressed()
        if args[pygame.K_s]:
            self.rect.top += 5
        if args[pygame.K_SPACE]:
            self.rect.top -= 5
        if args[pygame.K_d]:
            self.rect.right += 5
        if args[pygame.K_a]:
            self.rect.right -= 5
