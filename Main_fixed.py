import pygame
from pygame import display
from Table_file import Card_table
from World_file import World, data, bg
from Arrow_file import Arrow
from Card_init_file import CardInnit, FirstMonster, SecondMonster, ThirdMonster, \
    FourthMonster, FifthMonster, SixMonster

if __name__ == '__main__':
    pygame.init()
    display.set_caption('Монстрики/Монстры')
    size = width, height = 1600, 800
    screen = display.set_mode(size)
    fps = 60
    tile = 50

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    world = World(data, tile, screen)
    table = Card_table(screen)
    cards = CardInnit()
    Monsters_name_list = cards.give_cards()
    print(Monsters_name_list)

    First_monster = FirstMonster(all_sprites, screen, Monsters_name_list[0])
    Second_monster = SecondMonster(all_sprites, screen, Monsters_name_list[1])
    Third_monster = ThirdMonster(all_sprites, screen, Monsters_name_list[2])
    Fourth_Monster = FourthMonster(all_sprites, screen, Monsters_name_list[3])
    Fifth_Monster = FifthMonster(all_sprites, screen, Monsters_name_list[4])
    Six_Monster = SixMonster(all_sprites, screen, Monsters_name_list[5])



    arrow = Arrow(all_sprites, screen)
    running = True

    while running:
        screen.blit(bg, (0, 0))
        world.draw()
        table.draw()

        table = Card_table(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key:
                all_sprites.update(key)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

    clock.tick(fps)
    pygame.quit()
