import pygame
from pygame import mixer
from pygame import display
from Button import Button
from Table_file import Card_table
from World_file import World, back_ground, kristall_group
from Arrow_file import Arrow
from Card_init_file import CardInnit, FirstMonster, SecondMonster, ThirdMonster, \
    FourthMonster, FifthMonster, SixMonster
from Pers_file import Pers
from Kristall import Kristall

from Card_init_file import FirstKristall, SecondKristall, ThirdKristall, FourthKristall

first_level_data = [
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'A'],
    ['X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 1, '.', 'X', 'X', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'A', 'X', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', '.', '.', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'l', 'l', 'l', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', ]]

# data = open('First_world_data.txt', 'r')

second_level_data = [
    ['X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', '.', '.',
     'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', '.', '.', 'X', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.''X', 'A', 'X', '.', '.', '.', 'X', '.', '.', '.',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', 'X', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', 'A', 'X', 'X', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'x'],
    ['X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', 'X', '.',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', ]]

if __name__ == '__main__':
    pygame.mixer.pre_init()
    pygame.init()
    display.set_caption('Монстрики/Монстры')

    size = width, height = 1600, 800

    screen = display.set_mode(size)
    fps = 60
    tile_x, tile_y = 70, 50
    menu = True

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # ---------------ЗВУКИ---------------

    # создание основных объектов
    score = 0
    image_start = pygame.image.load('game_imgs/Start.png')
    image_start = pygame.transform.scale(image_start, (484, 131))
    bg = pygame.image.load('game_imgs\Back.jpg')
    bg = pygame.transform.scale(bg, (width, height))
    button = Button(width, height, image_start, screen)
    world = World(first_level_data, tile_x, tile_y, screen)
    tilelst = world.get_tilelst()
    num_of_data = 1
    table = Card_table(screen)
    cards = CardInnit()
    pers = Pers(all_sprites, tilelst)

    # создание списков названий монстров, еды и времени сна
    Monsters_name_list = cards.get_monster_cards()
    # print(Monsters_name_list)
    # Food_list = cards.get_food_cards()
    # # print(Food_list)
    # Time_list = cards.get_sleeping_time()
    # print(Time_list)

    # ---------------создание первых трех карточек МОНСТРИКОВ---------------
    First_monster = FirstMonster(all_sprites, screen, Monsters_name_list[0])
    Second_monster = SecondMonster(all_sprites, screen, Monsters_name_list[1])
    Third_monster = ThirdMonster(all_sprites, screen, Monsters_name_list[2])
    Fourth_Monster = None
    Fifth_Monster = None
    Six_Monster = None

    # ---------------создание первых четырех карточек ЕДЫ---------------

    # First_Food = FirstFood(all_sprites, screen, Food_list[0])
    # Second_Food = SecondFood(all_sprites, screen, Food_list[1])
    # Third_Food = None
    # Fourth_Food = None
    First_kris_card = FirstKristall(all_sprites, screen)
    Second_kris_card = SecondKristall(all_sprites, screen)
    Third_kris_card = ThirdKristall(all_sprites, screen)
    Fourth_kris_card = FourthKristall(all_sprites, screen)

    arrow = Arrow(all_sprites, screen)
    running = True
    print(score)
    can_update_arr = True
    now = 1
    last = 1

    while running:
        clock.tick(fps)
        if menu:
            screen.blit(bg, (0, 0))
            if button.draw():
                menu = False
        else:
            screen.blit(back_ground, (0, 0))
            if pygame.sprite.spritecollide(pers, kristall_group, True):
                score += 1
                if First_kris_card.get_count() < 4:
                    First_kris_card.plus_one()
                elif Second_kris_card.get_count() < 4:
                    Second_kris_card.plus_one()
                elif Third_kris_card.get_count() < 4:
                    Third_kris_card.plus_one()
                elif Fourth_kris_card.get_count() < 4:
                    Fourth_kris_card.plus_one()
                else:
                    pass
            # вывести сообщение о переполненном инвентаре

            kristall_group.draw(screen)
            world.draw()
            table.draw()

            table = Card_table(screen)

            # смена уровней. пока костыльно
            pers_x = pers.get_cords()

            num_of_data = world.get_num_of_data()
            if num_of_data == 2 and pers_x >= 1500:
                world = World(second_level_data, tile_x, tile_y, screen)
            if num_of_data == 1 and pers_x <= 100:
                world = World(first_level_data, tile_x, tile_y, screen)
            key = pygame.key.get_pressed()
            if key:
                all_sprites.update()
                kristall_group.update()
                # обновление мира
                world.updating_world(pers_x, num_of_data)

            if pers_x >= 1500 and num_of_data == 1:
                main_data = second_level_data
                world = World(main_data, tile_x, tile_y, screen)
                new_tilelst = world.get_tilelst()
                pers.change_tilelst(new_tilelst)
                num_of_data = 2
                pers.move_pers_back()
            elif pers_x <= 15 and num_of_data == 2:
                main_data = first_level_data
                world = World(main_data, tile_x, tile_y, screen)
                new_tilelst = world.get_tilelst()
                pers.change_tilelst(new_tilelst)
                num_of_data = 1
                pers.move_pers_foward()


            all_sprites.draw(screen)
            all_sprites.update()

            if can_update_arr and arrow.get_args():
                arrow.update_arrow()

                can_update_arr = False
                last = None
                if not last:
                    last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            if now - last >= 200:
                can_update_arr = True
            kristall_group.update()
            print(now, last)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    clock.tick(fps)
    pygame.quit()
