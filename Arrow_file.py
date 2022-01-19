import pygame
from Card_init_file import CardInnit, FirstMonster, SecondMonster, ThirdMonster, \
    FourthMonster, FifthMonster, SixMonster


class Arrow(pygame.sprite.Sprite):
    image = pygame.image.load('game_imgs\Table.png')

    def __init__(self, group, screen):
        super().__init__(group)
        self.screen = screen
        self.monster_arrow_image = pygame.image.load('game_imgs\Monster_arrow.png')
        self.food_arrow_image = pygame.image.load('game_imgs\Food_arrow.png')

        self.rect = self.monster_arrow_image.get_rect()
        self.rect.x = 19
        self.rect.y = 614

        self.monster_arrow_poz = 1  # позиция курсора при выборе монстрика
        self.monster_card_quantity = 3  # количество карт монстриков (изначально - 3)
        self.max_monsters_quantity = 6  # максимальное количество карт монстриков
        self.monster_move_length = 188  # расстояние перемещения курсора при выборе монстрика

        self.food_arrow_poz = 1  # позиция курсора при выборе корма
        self.food_move_length_left = 204  # расстояние перемещения курсора в влево при выборе еды
        self.food_move_length_down = 84  # расстояние перемещения курсора в вниз при выборе еды
        self.food_card_quantity = 2  # количество карт корма (изначально - 2)
        self.max_food_quantity = 4  # максимальное количество карт корма

        self.caught_food = False  # Значение, отвечающее за взятую после нажатия еду
        # за сами карты монстриков и корма отвечает отдельный класс,
        # из которого сюда передается значение при взаимодействии

        self.arrow_poz = "Monst"  # Флаг распознания локации курсора

        self.image = self.monster_arrow_image

    def update_arrow(self):
        args = pygame.key.get_pressed()
        if self.arrow_poz == "Monst":  # если курсор в зоне карт с монстрами
            if args and args[pygame.K_LEFT]:
                if self.monster_arrow_poz > 1:
                    self.rect.left -= self.monster_move_length
                    self.monster_arrow_poz -= 1
                    # print(self.arrow_poz)


            if args and args[pygame.K_RIGHT]:
                if self.monster_arrow_poz < self.max_monsters_quantity:
                    self.rect.left += self.monster_move_length
                    self.monster_arrow_poz += 1
                    # print(self.rect.x)
                    # print(self.arrow_poz)

            if args and args[pygame.K_RCTRL]:
                self.image = self.food_arrow_image

                self.rect.x = 1170
                self.rect.y = 615
                self.arrow_poz = "Food"
                self.food_arrow_poz = 1

            if args and args[pygame.K_RETURN]:
                if self.monster_arrow_poz <= self.monster_card_quantity:
                    print('Monster card activated')  # вывод сообщения

                    self.monster_card_quantity -= 1
                else:
                    if self.monster_card_quantity > 0:
                        print('This monster slot is blank')  # вывод сообщения
                    else:
                        print("You'v not any monsters")  # вывод сообщения

            if args and args[pygame.K_RSHIFT]:
                if self.caught_food:  # если корм был выбран, монстрика можно покормить выбранным кормом
                    if self.monster_arrow_poz <= self.monster_card_quantity:
                        print('Monster fed')
                        self.caught_food = False
                    else:
                        print("This monster slot is blank. You can't feed an emptiness")
                else:
                    print("Food wasn't chosen")


        # --------------------------FOOD-------------------------
        elif self.arrow_poz == "Food":  # если курсор в зоне карт с кормом
            if args and args[pygame.K_LEFT]:
                if self.food_arrow_poz == 2 or self.food_arrow_poz == 4:
                    self.rect.left -= self.food_move_length_left
                    self.food_arrow_poz -= 1
                    # print(self.food_arrow_poz)

            if args and args[pygame.K_RIGHT]:
                if self.food_arrow_poz == 1 or self.food_arrow_poz == 3:
                    self.rect.left += self.food_move_length_left
                    self.food_arrow_poz += 1
                    # print(self.food_arrow_poz)

            if args and args[pygame.K_UP]:
                if self.food_arrow_poz == 3 or self.food_arrow_poz == 4:
                    self.rect.top -= self.food_move_length_down
                    self.food_arrow_poz -= 2

            if args and args[pygame.K_DOWN]:
                if self.food_arrow_poz == 1 or self.food_arrow_poz == 2:
                    self.rect.top += self.food_move_length_down
                    self.food_arrow_poz += 2

            if args and args[pygame.K_RCTRL]:
                self.image = self.monster_arrow_image

                self.rect.x = 20
                self.rect.y = 614
                self.arrow_poz = "Monst"
                self.monster_arrow_poz = 1

            if args and args[pygame.K_RSHIFT]:
                if self.food_arrow_poz <= self.food_card_quantity:
                    print('Food was chosen')  # вывод сообщения)
                    self.food_card_quantity -= 1
                    self.caught_food = True  # это значение будет заменено на конкретное, взятое из класса CardInnit
                    # исходя из этого значения будет приниматься решение о варианте взаимодействия с картой
                    # (выбор/ замена (при уже выбранной карте))
                else:
                    if self.food_card_quantity > 0:
                        print('This food slot is blank')  # вывод сообщения
                    else:
                        print("You'v not any food")  # вывод сообщения

    def get_args(self):
        args = pygame.key.get_pressed()
        if args and args[pygame.K_LEFT]:
            return 1
        if args and args[pygame.K_RIGHT]:
            return 1
        if args and args[pygame.K_UP]:
            return 1
        if args and args[pygame.K_DOWN]:
            return 1
        if args and args[pygame.K_RCTRL]:
            return 1
        if args and args[pygame.K_RSHIFT]:
            return 1
        if args and args[pygame.K_RETURN]:
            return 1
        return 0
