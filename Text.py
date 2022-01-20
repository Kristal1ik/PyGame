import pygame
from pygame import display


class Text:
    def __init__(self, text, w, h):
        self.text = text
        self.color = (0, 0, 0)
        self.size = 35
        self.font = "Helvetica"
        self.w = w
        self.h = h
        size = self.w, self.h
        self.screen = display.set_mode(size)

    def create(self):
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, True, self.color)
        self.screen.blit(text, (self.w // 2, self.h // 2))

