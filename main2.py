import pygame
from pygame import display
from Table_file import Card_table
from World_file import World, data, bg
#from Arrow_file import Arrow

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    display.set_caption("Монстрики/Монстры")
    running = True
    fps = 60
    tile = 50
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()


    # pers = pygame.image.load()


    world = World(data, tile, screen)
    cards = Card_table(screen)

    while running:
        screen.blit(bg, (0, 0))
        world.draw()


        cards.draw()
        
        #cards.arrow()
        # screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            key = pygame.key.get_pressed()
            if key:
                all_sprites.update(key)

        pygame.display.update()
    clock.tick(fps)

    pygame.quit()
