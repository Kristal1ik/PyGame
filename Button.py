import pygame


class Button:
    def __init__(self, x, y, image, screen):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x // 2 - 240
        self.rect.y = y // 2 - 70
        self.clicked = False

    def draw(self):
        f = False

        # Мышка
        pos = pygame.mouse.get_pos()

        # Проверка
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                f = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # отрисовка кнопки
        self.screen.blit(self.image, self.rect)

        return f
