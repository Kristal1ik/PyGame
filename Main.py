import pygame
# from start_window import Start_window, buttons_rect
from pygame import display
from Button import Button
from pygame import mixer
from Table_file import Card_table
from World_file import World, back_ground, kristall_group
from Arrow_file import Arrow
from Card_init_file import CardInnit, FirstMonster, SecondMonster, ThirdMonster, \
    FourthMonster, FifthMonster, SixMonster
from Pers_file import Pers, get_sound
from Kristall import Kristall

from Card_init_file import FirstKristall, SecondKristall, ThirdKristall, FourthKristall

first_level_data = [
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'A'],
    ['X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 1, 'X', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 1, '.', 'X', 'X', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', 'X', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', 1, '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', '.', '.', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'l', 'l', 'l', '.', '.', '.', '.', '.', '.', 1, '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', ]]

# data = open('First_world_data.txt', 'r')

second_level_data = [
    ['X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', '.', '.',
     'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', '.', '.', 'X', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', 1, '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.''X', 'A', 'X', '.', '.', '.', 'X', '.', '.', '.',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', '.', '.', 1, '.', '.', '.', '.', '.', '.', '.', 1, 'X', 'X', 'X', 'X', 'X', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', 'X', '.', '.', 'X', 'X', '.', '.', 'A', 'X', 'X', 'X',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['X', 'X', 'X', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', 'X', '.',
     '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.']]

third_level_data = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', ]]

if __name__ == '__main__':

    pygame.init()
    display.set_caption('Монстрики/Монстры')

    size = width, height = 1600, 800

    screen = display.set_mode(size)
    fps = 60
    tile_x, tile_y = 70, 50
    menu = True

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # создание основных объектов
    score = 0
    back_ground_with_boss = pygame.image.load('game_imgs/Boss.jpg')
    back_ground_with_boss1 = pygame.image.load('game_imgs/Boss1.jpg')
    image_start = pygame.image.load('game_imgs/Start.png')
    image_start = pygame.transform.scale(image_start, (484, 131))
    bg = pygame.image.load('game_imgs\Back.jpg')
    bg = pygame.transform.scale(bg, (width, height))
    end = pygame.image.load('game_imgs\End.jpg')
    end = pygame.transform.scale(end, (width, height))
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
    Fourth_Monster = FourthMonster(all_sprites, screen, Monsters_name_list[3])
    Fifth_Monster = FifthMonster(all_sprites, screen, Monsters_name_list[4])
    Six_Monster = SixMonster(all_sprites, screen, Monsters_name_list[5])

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
    can_update_arr = True
    now = 1
    last = 1
    last_world = False
    i = 0
    last_count = 0
    count_of_attacks = 0
    while running:
        i += 1
        clock.tick(fps)
        if menu:
            screen.blit(bg, (0, 0))
            if button.draw():
                menu = False
        else:
            if last_world:
                if i % 40 == 0:
                    bg = back_ground_with_boss1
                elif i % 20 == 0:
                    bg = back_ground_with_boss
                screen.blit(bg, (0, 0))
            else:
                screen.blit(back_ground, (0, 0))
            if pygame.sprite.spritecollide(pers, kristall_group, True):
                get_sound.play()
                score += 1

                if First_kris_card.get_count() < 4:
                    First_kris_card.plus_one()
                elif Second_kris_card.get_count() < 4:
                    Second_kris_card.plus_one()
                elif Third_kris_card.get_count() < 4:
                    Third_kris_card.plus_one()
                elif Fourth_kris_card.get_count() < 4:
                    Fourth_kris_card.plus_one()
                last_count = score
                arrow.food_card_quantity = First_kris_card.get_count()

            now_score = arrow.get_count_kris()
            print(now_score, last_count)
            is_monstr_activated = arrow.get_is_ret_monst()
            print(is_monstr_activated)
            if is_monstr_activated and now_score > 1:
                now_score -= 2
                monstr_activated = True
                if Fourth_kris_card.get_count() > 0:
                    Fourth_kris_card.count -= 1
                    Fourth_kris_card.image = pygame.image.load(
                        f'game_imgs/Kristals/Card_Kris{Fourth_kris_card.count}.png')
                elif Third_kris_card.get_count() > 0:
                    Third_kris_card.count -= 1
                    Third_kris_card.image = pygame.image.load(
                        f'game_imgs/Kristals/Card_Kris{Third_kris_card.count}.png')
                elif Second_kris_card.get_count() > 0:
                    Second_kris_card.count -= 1
                    Second_kris_card.image = pygame.image.load(
                        f'game_imgs/Kristals/Card_Kris{Second_kris_card.count}.png')
                elif First_kris_card.get_count() > 0:
                    First_kris_card.count -= 1
                    First_kris_card.image = pygame.image.load(
                        f'game_imgs/Kristals/Card_Kris{First_kris_card.count}.png')
                else:
                    monstr_activated = False
                num_of_mon_card = arrow.get_activated_card()
                print(num_of_mon_card)
                if monstr_activated:
                    if First_monster:
                        if First_monster.get_num() == num_of_mon_card:
                            First_monster = Second_monster
                            Second_monster = Third_monster
                            Third_monster = Fourth_Monster
                            Fourth_Monster = Fifth_Monster
                            Fifth_Monster = Six_Monster
                            First_monster.rect.x -= 188
                            if Second_monster:
                                Second_monster.rect.x -= 188
                            if Third_monster:
                                Third_monster.rect.x -= 188
                            if Fourth_Monster:
                                Fourth_Monster.rect.x -= 188
                            if Fifth_Monster:
                                Fifth_Monster.rect.x -= 188
                            Six_Monster = None
                    if Second_monster:
                        if Second_monster.get_num() == num_of_mon_card:
                            Second_monster, Third_monster, Fourth_Monster, Fifth_Monster, \
                            Six_Monster = Third_monster, Fourth_Monster, Fifth_Monster, Six_Monster, None
                            Second_monster.rect.x -= 188
                            if Third_monster:
                                Third_monster.rect.x -= 188
                            if Fourth_Monster:
                                Fourth_Monster.rect.x -= 188
                            if Fifth_Monster:
                                Fifth_Monster.rect.x -= 188
                    if Third_monster:
                        if Third_monster.get_num() == num_of_mon_card:
                            Third_monster, Fourth_Monster, Fifth_Monster, \
                            Six_Monster = Fourth_Monster, Fifth_Monster, Six_Monster, None
                            Third_monster.rect.x -= 188
                            if Fourth_Monster:
                                Fourth_Monster.rect.x -= 188
                            if Fifth_Monster:
                                Fifth_Monster.rect.x -= 188
                    if Fourth_Monster:
                        if Fourth_Monster.get_num() == num_of_mon_card:
                            Fourth_Monster, Fifth_Monster, \
                            Six_Monster = Fifth_Monster, Six_Monster, None
                            Fourth_Monster.rect.x -= 188
                            if Fifth_Monster:
                                Fifth_Monster.rect.x -= 188
                    if Fifth_Monster:
                        if Fifth_Monster.get_num() == num_of_mon_card:
                            Fifth_Monster, \
                            Six_Monster = Six_Monster, None
                            if Fifth_Monster:
                                Fifth_Monster.rect.x -= 188
                    if Six_Monster:
                        if Six_Monster.get_num() == num_of_mon_card:
                            Six_Monster = None
                    count_of_attacks += 1  # СЧЕТТТТТТТТТТТТЧИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИК
                if count_of_attacks == 2:
                    ending = True
                    while ending:
                        screen.blit(end, (0, 0))

            # вывести сообщение о переполненном инвентаре

            kristall_group.draw(screen)
            world.draw()
            table.draw()

            table = Card_table(screen)

            # смена уровней. пока костыльно
            pers_x = pers.get_cords()
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
            elif pers_x >= 1500 and num_of_data == 2:
                main_data = third_level_data
                world = World(main_data, tile_x, tile_y, screen)
                new_tilelst = world.get_tilelst()
                pers.change_tilelst(new_tilelst)
                num_of_data = 3
                last_world = True
                pers.move_pers_back()
            elif pers_x <= 15 and num_of_data == 3:
                main_data = second_level_data
                world = World(main_data, tile_x, tile_y, screen)
                new_tilelst = world.get_tilelst()
                pers.change_tilelst(new_tilelst)
                num_of_data = 2
                last_world = False
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
            # print(now, last)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    clock.tick(fps)
    pygame.quit()
