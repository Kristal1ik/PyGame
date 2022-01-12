import pygame
import os
FPS = 60

class Start_window:

    def __init__(self):
        self.width, self.height = 1280, 601
        # self.running, self.moving = True, False

    def draw(self):
        buttons_surf = pygame.image.load('game_imgs\Buttons.png')
        bg = pygame.image.load('game_imgs\Back.jpg')
        buttons_surf = pygame.transform.scale(
            buttons_surf, (buttons_surf.get_width() // 2,
                           buttons_surf.get_height() // 2))

        buttons_rect = buttons_surf.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(bg, (0, 0))

        screen.blit(buttons_surf, buttons_rect)
        pygame.display.update()

        # проверка координат
        # pygame.draw.rect(self.screen, pygame.Color('red'), (112, 81, 475, 125), 0)
        #
        # pygame.draw.rect(self.screen, pygame.Color(0, 255, 0, 0), (172, 242, 356, 75), 0)
        #
        # pygame.draw.rect(self.screen, pygame.Color(0, 0, 255, a=0), (172, 342, 356, 75), 0)

    def run(self):
        running = True
        while running:
            # screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(FPS)
            #
            # self.start_pos_x1, self.start_pos_y1 = 112, 81
            # self.start_pos_x2, self.start_pos_y2 = 112 + 475, 81 + 125
            #
            # self.sett_pos_x1, self.sett_pos_y1 = 172, 242
            # self.sett_pos_x2, self.sett_pos_y2 = 172 + 356, 242 + 75
            #
            # self.about_pos_x1, self.about_pos_y1 = 172, 342
            # self.about_pos_x2, self.about_pos_y2 = 172 + 356, 342 + 75
            #
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         self.running = False
            #
            #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #         if self.start_pos_x1 < event.pos[0] < self.start_pos_x2 and self.start_pos_y1 < event.pos[
            #             1] < self.start_pos_y2:
            #             print(1)
            #
            #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #         if self.sett_pos_x1 < event.pos[0] < self.sett_pos_x2 and self.sett_pos_y1 < event.pos[
            #             1] < self.sett_pos_y2:
            #             print(2)
            #
            #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #         if self.about_pos_x1 < event.pos[0] < self.about_pos_x2 and self.about_pos_y1 < event.pos[
            #             1] < self.about_pos_y2:
            #             print(3)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    size = 1280, 601
    screen = pygame.display.set_mode(size)

    start_win = Start_window()
    start_win.draw()
    start_win.run()

    pygame.quit()