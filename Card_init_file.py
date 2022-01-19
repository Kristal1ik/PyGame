import random
import pygame
import os


def name_generate(num, name):
    return f'Card_{name}{num}.png'


def way_generate(type, name):
    return os.path.join(f'game_imgs\{type}\{name}')


class CardInnit:  # определение монстров
    def __init__(self):
        self.Monsters = []
        self.Food = []
        self.food_list = [1, 2, 3, 4, 5, 6, 7, 8]  # список всей игровой еды
        # при возможности стоит добавить
        self.monsters_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # список всех монстриков
        self.variants_of_time = [10, 15, 20, 25, 30, 35, 40]  # список всех возможных вариантов продолжительности спячки
        self.monsters_parameters = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '',
                                    7: '', 8: '', 9: '', 10: '', 11: '', 12: ''}  # здесь будут записаны характеристики

    # Случайная генерация имен (названий файлов .png) монстриков
    def get_monster_cards(self):
        self.monster_probability = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]  # вероятность выпадения той или иной
        # карты монстрика соответственно, в пропорциональном отношении
        self.monster_nums = random.choices(self.monsters_names, weights=self.monster_probability, k=3)

        self.numbers_of_monster = []
        for i in range(len(self.monster_nums)):
            self.numbers_of_monster.append(self.monster_nums[i])
            self.Monsters.append(name_generate(self.monster_nums[i], 'Monster'))
        #  print(self.Monsters)
        return self.Monsters

    # генерация имен карточек еды
    # def get_food_cards(self):
    #     self.food_probability = [4, 4, 3, 3, 3, 2, 2, 1]  # вероятность выпадения той или иной
    #     # карты еды соответственно, в пропорциональном отношении
    #     self.food_nums = random.choices(self.food_list, weights=self.food_probability, k=4)
    #     # print(self.Monster_cards, self.Food_cards)
    #
    #     self.numbers_of_food = []
    #     for i in range(len(self.food_nums)):
    #         self.numbers_of_food.append(self.food_nums[i])
    #         self.Food.append(name_generate(self.food_nums[i], 'Food'))
    #     #  print(self.Food)
    #     return self.Food

    # генерация времени спячки для каждого монстрика
    # def get_sleeping_time(self):
    #
    #     self.variants_of_time_probability = [10, 15, 20, 20, 25, 10, 5]  # позже можно будет добавить
    #     # изменение вероятности выпадения той или иной спячки со временем
    #     self.Sleeping_time = random.choices(self.variants_of_time, weights=self.variants_of_time_probability, k=3)
    #     return self.Sleeping_time


# Далее - классы монстриков - по классу на каждый СЛОТ
class FirstMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26
        self.rect.y = 620

        self.baf = 20  # урон от бафа от корма (если будет)
        self.sleeping_time = 20  # время спячки

    def activated(self):
        self.hitpoint = 100  # значение урона (по ходу продакешна может изменится)
        self.new_image = 1  # создастся новое временное изображение на время анимации атаки
        self.activated_card = True



class SecondMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + 180 + 8
        self.rect.y = 620


class ThirdMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 2
        self.rect.y = 620


class FourthMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 3
        self.rect.y = 620


class FifthMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 4
        self.rect.y = 620


class SixMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        self.screen = screen

        # monster_name будет инициализироваться в init_new_card.
        # Лучше создать отдельный метод для всех слотов
        self.monster_name = way_generate('Monsters', monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 5
        self.rect.y = 620


class FirstFood(pygame.sprite.Sprite):
    def __init__(self, group, screen, food_name):
        super().__init__(group)
        self.group = group
        self.screen = screen

        self.food_name = way_generate('Food', food_name)
        self.image = pygame.image.load(self.food_name)
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620


class SecondFood(pygame.sprite.Sprite):
    def __init__(self, group, screen, food_name):
        super().__init__(group)
        self.group = group
        self.screen = screen

        self.food_name = way_generate('Food', food_name)
        self.image = pygame.image.load(self.food_name)
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620


class ThirdFood(pygame.sprite.Sprite):
    def __init__(self, group, screen, food_name):
        super().__init__(group)
        self.group = group
        self.screen = screen

        self.food_name = way_generate('Food', food_name)
        self.image = pygame.image.load(self.food_name)
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620 + 76 + 8


class FourthFood(pygame.sprite.Sprite):
    def __init__(self, group, screen, food_name):
        super().__init__(group)
        self.group = group
        self.screen = screen

        self.food_name = way_generate('Food', food_name)
        self.image = pygame.image.load(self.food_name)
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620 + 76 + 8


class FirstKristall(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)

        self.group = group
        self.screen = screen
        self.count = 0
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620

    def plus_one(self):
        self.count += 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620

    def minus_one(self):
        self.count -= 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620

    def get_count(self):
        return self.count


class SecondKristall(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)

        self.group = group
        self.screen = screen
        self.count = 0
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620

    def plus_one(self):
        self.count += 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620

    def minus_one(self):
        self.count -= 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620

    def get_count(self):
        return self.count

class ThirdKristall(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)

        self.group = group
        self.screen = screen
        self.count = 0
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620 + 76 + 8

    def plus_one(self):
        self.count += 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620 + 76 + 8

    def minus_one(self):
        self.count -= 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176
        self.rect.y = 620 + 76 + 8

    def get_count(self):
        return self.count

class FourthKristall(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)

        self.group = group
        self.screen = screen
        self.count = 0
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620 + 76 + 8

    def plus_one(self):
        self.count += 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620 + 76 + 8

    def minus_one(self):
        self.count -= 1
        self.image = pygame.image.load(f'game_imgs/Kristals/Card_Kris{self.count}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1176 + 196 + 8
        self.rect.y = 620 + 76 + 8

    def get_count(self):
        return self.count
