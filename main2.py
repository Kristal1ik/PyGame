import pygame
from pygame import display


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    display.set_caption("Монстрики/Монстры")

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
