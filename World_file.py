import pygame
from Kristall import Kristall

back_ground = pygame.image.load('game_imgs/Back_ground.jpg')

kristall_group = pygame.sprite.Group()


class World:
    def __init__(self, data, tile_x, tile_y, screen):
        self.tilelst = []
        self.num_of_data = 1
        self.screen = screen
        self.block = pygame.image.load('game_imgs/Block.png')
        self.block = pygame.transform.scale(self.block, (70, 50))
        self.kristall = pygame.image.load('game_imgs/Kristall1.png')
        self.kristall = pygame.transform.scale(self.kristall, (36, 30))

        n_row = 0
        for i in data:
            n = 0
            for j in i:
                if j == 'X' or j == 2 or j == 'A':  # A - armor. if it'll be time, i can make
                    image = self.block
                    rect = image.get_rect()
                    rect.x = n * tile_x
                    rect.y = n_row * tile_y
                    j = (image, rect)
                    self.tilelst.append(j)
                elif j == 1:

                    kristall = Kristall(n * tile_x + (tile_x // 2), n_row * tile_y + (tile_y // 2))
                    kristall_group.add(kristall)
                    print(kristall.get_rect())


                n += 1
            n_row += 1
        # print(kristall_group)


    def draw(self):
        for i in self.tilelst:
            self.screen.blit(i[0], i[1])
            # print(i)

    def get_tilelst(self):
        return self.tilelst

    def get_num_of_data(self):
        return self.num_of_data


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
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', 1, '.', '.', '.', '.'],
    ['.', '.', '.', '.', 1, '.', '.', '.', '.', '.', 'X', '.', '.''X', 'A', 'X', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'A', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', '.', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', 'X', 'X', '.', '.', 'A', 'X', 'X', 'X', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.''X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.']]

third_level_data = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X','X', 'X', 'X', 'X', 'X', 'X',
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
