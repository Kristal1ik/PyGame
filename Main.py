import pygame
from pygame import display
from Table_file import Card_table
from World_file import World, data, back_ground
from Arrow_file import Arrow
from Card_init_file import CardInnit, FirstMonster, SecondMonster, ThirdMonster, \
    FourthMonster, FifthMonster, SixMonster
from Pers_file import Pers

from Card_init_file import FirstFood, SecondFood, ThirdFood, FourthFood

if __name__ == '__main__':
    pygame.init()
    display.set_caption('Монстрики/Монстры')
    size = width, height = 1600, 800
    screen = display.set_mode(size)
    fps = 60
    tile = 50

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # создание основных объектов
    world = World(data, tile, screen)
    table = Card_table(screen)
    cards = CardInnit()
    pers = Pers(all_sprites)
    # создание списков названий монстров, еды и времени сна
    Monsters_name_list = cards.get_monster_cards()
    print(Monsters_name_list)
    Food_list = cards.get_food_cards()
    print(Food_list)
    Time_list = cards.get_sleeping_time()
    print(Time_list)

    # ---------------создание первых трех карточек МОНСТРИКОВ---------------
    First_monster = FirstMonster(all_sprites, screen, Monsters_name_list[0], Time_list[0])
    Second_monster = SecondMonster(all_sprites, screen, Monsters_name_list[1], Time_list[1])
    Third_monster = ThirdMonster(all_sprites, screen, Monsters_name_list[2], Time_list[2])
    Fourth_Monster = None
    Fifth_Monster = None
    Six_Monster = None

    # ---------------создание первых четырех карточек ЕДЫ---------------

    First_Food = FirstFood(all_sprites, screen, Food_list[0])
    Second_Food = SecondFood(all_sprites, screen, Food_list[1])
    Third_Food = None
    Fourth_Food = None

    arrow = Arrow(all_sprites, screen)
    running = True

    while running:
        screen.blit(back_ground, (0, 0))
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
