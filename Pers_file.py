import pygame
from World_file import tilelst
import pickle
from os import path
from pygame import Rect


class Pers(pygame.sprite.Sprite):

    # у персонажа изначальный размер = 100 * 60 пикселей

    def __init__(self, group):
        super().__init__(group)
        self.images = []
        for i in range(1, 6):
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        # Изменены клавиши управления, чтобы при работе не было конфликта с классом Arrow.
        # Теперь управление как в большинстве игр - WASD

        # Упращено
        dx = 0
        dy = 0
        clock = pygame.time.Clock()
        time = 5
        fps = 60
        f = 1  # Проверка на то, нажат ли пробел
        args = pygame.key.get_pressed()
        if args[pygame.K_s]:
            dy += 5
        if args[pygame.K_SPACE] and f == 1:
            f = 0
            self.vy = -15

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
                self.image = self.images[4]
            else:
                self.image = pygame.transform.flip(self.images[2], True, False)

        # Гравитация
        self.vy += 1
        if self.vy > 10:
            self.vy = 10
        dy += self.vy

        # Столкновение
        for i in tilelst:
            if i[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            if i[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # Столкновение при прыжке
                if self.vy < 0:
                    dy = i[1].bottom - self.rect.top
                    self.vy = 0
                    f = 0
                # Столкновение при падении
                elif self.vy >= 0:
                    dy = i[1].top - self.rect.bottom
                    f = 1

                    self.vy = 0


        self.rect.x += dx
        self.rect.y += dy

    def get_cords(self):
        return self.rect.x



