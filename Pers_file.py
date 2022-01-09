import pygame


class Pers(pygame.sprite.Sprite):

    # у персонажа изначальный размер = 100 * 60 пикселей

    def __init__(self, group):
        super().__init__(group)
        self.images = []
        for i in range(1, 5):
            image = pygame.image.load(f'Кадры анимации персонажей + gif\Peres_anim_cadr{i}.png')
            self.images.append(image)
        self.image = self.images[0]
        self.n = 0  # индекс
        self.nn = 0  # для анимации
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 450
        self.vy = 0
        self.side = 0

    def update(self):
        # Изменены клавиши управления, чтобы при работе не было конфликта с классом Arrow.
        # Теперь управление как в большинстве игр - WASD

        # Упращено
        dx = 0
        dy = 0
        clock = pygame.time.Clock()
        time = 5
        fps = 60
        f = False  # Проверка на то, нажат ли пробел
        args = pygame.key.get_pressed()
        if args[pygame.K_s]:
            dy += 5
        if args[pygame.K_SPACE] and not f:
            self.vy = -15
            f = True
        if args[pygame.K_SPACE]:
            f = False
        if args[pygame.K_d]:
            dx += 5

            # анимация
            self.side = 1
            self.nn += 1
            if self.nn > time:
                self.nn = 0
                self.n += 1
                if self.n >= len(self.images):
                    self.n = 0
                self.image = self.images[self.n]
        if args[pygame.K_a]:
            dx -= 5
            # анимация
            self.side = -1
            self.nn += 1
            if self.nn > time:
                self.nn = 0
                self.n += 1
                if self.n >= len(self.images):
                    self.n = 0
                self.image = pygame.transform.flip(self.images[self.n], True, False)
        if not args[pygame.K_a] and not args[pygame.K_d]:
            if self.side == 1:
                self.image = self.images[2]
            else:
                self.image = pygame.transform.flip(self.images[2], True, False)





        # Гравитация
        self.vy += 1
        if self.vy > 10:
            self.vy = 10
        dy += self.vy

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > 560:
            self.rect.bottom = 560
            dy = 0
