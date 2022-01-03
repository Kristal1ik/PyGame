import pygame


class Card_table():
    def __init__(self, screen):
        self.screen = screen
        self.height, self.width = 200, 1600

    def cards(self):
        self.max_col_csrds = 12

    def draw(self):
        # pygame.draw.rect(self.screen, pygame.Color('red'), (0, (800 - self.height), self.width, self.height), 0)
        self.table_surf = pygame.image.load('game_imgs\Table.png')
        self.table_rect = self.table_surf.get_rect(bottomright=(self.width, 800))
        self.screen.blit(self.table_surf, self.table_rect)
        pygame.display.update()

