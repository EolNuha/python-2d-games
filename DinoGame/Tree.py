import pygame
from Eagle import eagle

class tree(eagle):
    img = pygame.image.load('images/8.png')

    def draw(self, win):
        self.hitbox = (self.x, self.y, 30, 80)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


class SecondTree(eagle):
    img = pygame.image.load('images/7.png')

    def draw(self, win):
        self.hitbox = (self.x + 5, self.y, 67, 80)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False