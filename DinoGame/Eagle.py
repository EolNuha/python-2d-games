import pygame

class eagle(object):
    rotate = [pygame.image.load('images/5.png'),
              pygame.image.load('images/6.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.rotateCount >= 30:
            self.rotateCount = 0
        win.blit(pygame.transform.scale(self.rotate[self.rotateCount // 15], (64, 64)),
                 (self.x, self.y))
        self.rotateCount += 1

    def collide(self, rect):
        if rect[1] + rect[3] > self.hitbox[1] and rect[1] < self.hitbox[1] + self.hitbox[3]:
            if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
                return True
        return False