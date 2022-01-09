import pygame

back_ground = pygame.image.load('game_imgs\Back_ground.png')


class World:
    def __init__(self, data, tile, screen):
        self.screen = screen
        self.tilelst = []
        self.block = pygame.image.load('game_imgs\Block.png')
        n_row = 0
        for i in data:
            n = 0
            for j in i:
                if j == 'X' or j == 2:
                    image = self.block
                    rect = image.get_rect()
                    rect.x = n * tile
                    rect.y = n_row * tile
                    j = (image, rect)
                    self.tilelst.append(j)
                n += 1
            n_row += 1

    def draw(self):
        for i in self.tilelst:
            self.screen.blit(i[0], i[1])
            print(i)


# data = [
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.', '.', ',', ',', ',', ',', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', '.', '.', '.', '.', '.', '.', '.', ',', ',', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.'],
#     ['.', ',', ',', ',', ',', ',', ',', ',', ',', ',', '.', ',', '.', ',', '.', '.', '.', '.', '.', '.'],
#     ['.', ',', ',', ',', ',', ',', '.', '.', '.', ',', ',', ',', ',', ',', '.', '.', '.', '.', '.', '.'],
#     ['.', ',', ',', ',', ',', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', ',', ',', ',', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# ]

data = [
    ['X', 'X', 'X', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-', 'X', 'X', 'X', 'X'],
    ['X', 'X', '-', '-', '-', '-', 'X', 'X', 'X', '-', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-', '-', 'X', 'X', 'X'],
    ['X', '-', '-', '-', '-', '-', 'X', 'X', '-', '-', 'X', 'X', 'X', '-', 'X', 'X', '-', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', '-', '-', '-', '-', 'X', 'X', 'X'],
    ['X', '-', '-', '-', '-', '-', 'X', '-', '-', '-', 'X', 'X', 'X', '-', 'X', 'X', '-', '-', '-', '-', 'X', 'X', 'X', 'X', 'X', '-', '-', '-', '-', '-', 'X', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-', 'X', 'X', '-', '-', '-', '-', '-', 'X', 'X', 'X', 'X', '-', '-', '-', '-', '-', 'X', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-', '-', '-', '-', '-', '-', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-', '-', '-', '-', '-', '-', 'X', '-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-', '-', 'X', 'X', '-', '-', 'X', '-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', '-', '-', '-', 'X', 'X', 'X', '-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', 'X', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'X', 'X', 'X', 'X', '-', '-', '-', '-', '-', 'X', '-', '-', '-', '-', '-', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

#data = open('First_world_data.txt', 'r')
