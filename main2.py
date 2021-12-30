import pygame
from pygame import display

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    display.set_caption("Монстрики/Монстры")
    running = True
    fps = 60
    clock = pygame.time.Clock()
    bg = pygame.image.load('bg.png')
    # pers = pygame.image.load()

    while running:
        screen.blit(bg, (0, 0))

        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    clock.tick(fps)

    pygame.quit()
