from game import Game
from game2 import Game2
from game3 import Game3
import pygame
import os

start_btn = pygame.image.load(os.path.join("game_assets", "easy.png"))
start_btn1 = pygame.image.load(os.path.join("game_assets", "normal.png"))
start_btn2 = pygame.image.load(os.path.join("game_assets", "hard.png"))
logo = pygame.image.load(os.path.join("game_assets", "title.png"))


class MainMenu:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width / 2 - start_btn1.get_width() / 2 - start_btn.get_width() - 20, 350, start_btn.get_width(),
                     start_btn.get_height())
        self.btn1 = (self.width / 2 - start_btn1.get_width() / 2, 350, start_btn1.get_width(), start_btn1.get_height())
        self.btn2 = (self.width / 2 - start_btn2.get_width() / 2 + start_btn1.get_width() + 20, 350, start_btn2.get_width(),
                     start_btn2.get_height())

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.run()
                            del game
                    elif self.btn1[0] <= x <= self.btn1[0] + self.btn1[2]:
                        if self.btn1[1] <= y <= self.btn1[1] + self.btn1[3]:
                            game2 = Game2(self.win)
                            game2.run()
                            del game2
                    elif self.btn2[0] <= x <= self.btn2[0] + self.btn2[2]:
                        if self.btn2[1] <= y <= self.btn2[1] + self.btn2[3]:
                            game3 = Game3(self.win)
                            game3.run()
                            del game3
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(logo, (self.width / 2 - logo.get_width() / 2, 50))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(start_btn1, (self.btn1[0], self.btn1[1]))
        self.win.blit(start_btn2, (self.btn2[0], self.btn2[1]))
        pygame.display.update()
