import random
import pygame
import os


def name_generate(num, name):
    return f'Card_{name}{num}.png'


def way_generate(name):
    return os.path.join(f'game_imgs\Monsters\{name}')


class CardInnit:  # определение монстров
    def __init__(self):
        self.Monsters = []
        self.food_list = [1, 2, 3, 4, 5, 6, 7, 8]  # список всей игровой еды
        self.monsters_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # список всех монстриков
        self.monsters_parameters = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '',
                                    7: '', 8: '', 9: '', 10: '', 11: '', 12: ''}  # здесь будут записаны характеристики

    # Случайная генерация имен монстриков
    def give_cards(self):
        self.monster_probability = [6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 1]  # вероятность выпадения той или иной
        # карты монстрика соответственно, в пропорциональном отношении
        self.monster_nums = random.choices(self.monsters_names, weights=self.monster_probability, k=6)

        self.food_probability = [4, 4, 3, 3, 3, 2, 2, 1]  # вероятность выпадения той или иной
        # карты еды соответственно, в пропорциональном отношении
        self.Food_cards = random.choices(self.food_list, weights=self.food_probability, k=4)

        # print(self.Monster_cards, self.Food_cards)

        self.numbers_of_monster = []
        for i in range(len(self.monster_nums)):
            self.numbers_of_monster.append(self.monster_nums[i])
            self.Monsters.append(name_generate(self.monster_nums[i], 'Monster'))
        #  print(self.Monsters)
        return self.Monsters


# Далее - классы монстриков - по классу на каждый СЛОТ
class FirstMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate(monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26
        self.rect.y = 620


class SecondMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate(monster_name)
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
        self.monster_name = way_generate(monster_name)
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
        self.monster_name = way_generate(monster_name)
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
        self.monster_name = way_generate(monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 4
        self.rect.y = 620


class SixMonster(pygame.sprite.Sprite):
    def __init__(self, group, screen, monster_name):
        super().__init__(group)
        self.group = group
        # self.monster_name = monster_name
        self.screen = screen
        # print(self.monster_name)
        self.monster_name = way_generate(monster_name)
        self.image = pygame.image.load(self.monster_name)
        self.rect = self.image.get_rect()
        self.rect.x = 26 + (180 + 8) * 5
        self.rect.y = 620
