import pygame


class player(object):
    run = [pygame.image.load('images/' + str(x) + '.png') for x in range(1, 3)]
    jump = pygame.image.load('images/10.png')
    slide = [pygame.image.load('images/3.png'),
             pygame.image.load('images/4.png')]
    fall = pygame.image.load('images/10.png')
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3,
                -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:

            win.blit(self.fall, (self.x, self.y + 30))

        elif self.jumping:

            self.y -= self.jumpList[self.jumpCount] * 4

            win.blit(self.jump, (self.x, self.y))

            self.jumpCount += 3

            if self.jumpCount > 108:
                self.jumpCount = 0

                self.jumping = False

                self.runCount = 0

            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
        elif self.sliding:
            if self.slideCount < 50:
                self.y = 440
                self.hitbox = (self.x + 4, self.y, self.width, self.height - 30)

            if self.slideCount >= 50:
                self.y = 410

            if self.slideCount >= 50:
                self.slideCount = 0
                self.runCount = 0
                self.sliding = False

                self.hitbox = (self.x + 4, self.y, self.width, self.height - 10)
            win.blit(self.slide[self.slideCount // 25], (self.x, self.y))
            self.slideCount += 1

        else:

            if self.runCount >= 12:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)

        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
