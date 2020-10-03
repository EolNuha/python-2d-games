import pygame
from pygame.locals import *
import random
from pygame import mixer
from Button import button, button1
from Eagle import eagle
from Player import player
from Tree import tree, SecondTree

W, H = 800, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Dinosaur Game')
icon = pygame.image.load('images/10.png')
pygame.display.set_icon(icon)


def enterWindow():
    Button = button((20, 20, 20), 310, 280, 150, 50, 'Play')
    bg = pygame.image.load('images/background2.jpg')
    go = True

    while go:
        win.blit(bg, (0, 0))
        Button.draw(win)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                go = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if Button.isOver(pos):
                    Button.color = (50, 50, 50)
                else:
                    Button.color = (70, 70, 70)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button.isOver(pos):
                    go = False

                    run = True

                    bg = pygame.image.load('images/background.jpg')
                    bgX = 0
                    bgX2 = bg.get_width()

                    clock = pygame.time.Clock()

                    def updateFile():
                        f = open('images/scores.txt', 'r')
                        file = f.readlines()
                        last = int(file[0])

                        if last < int(score):
                            f.close()
                            file = open('images/scores.txt', 'w')
                            file.write(str(score))
                            file.close()

                            return score

                        return last

                    def endScreen():
                        global score, speed, obstacles
                        speed = 60
                        obstacles = []
                        score = 0

                        run = True
                        while run:
                            for event in pygame.event.get():
                                keys = pygame.key.get_pressed()
                                if event.type == pygame.QUIT:
                                    run = False
                                    pygame.quit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    run = False
                                    runner.falling = False
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                                        run = False
                                        runner.falling = False

                            gameOver = pygame.image.load('images/GameOver.png')
                            win.blit(gameOver, (W / 2 - gameOver.get_width() / 2, H / 2 - gameOver.get_height() / 2))
                            largeFont = pygame.font.SysFont('comicsans', 60)
                            gameovertext = largeFont.render('Game Over', 1, (70, 70, 70))
                            win.blit(gameovertext, (W / 2 - gameovertext.get_width() / 2, 150))
                            pygame.display.update()

                    def pauseScreen():
                        run = True
                        while run:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    pygame.quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        run = False

                            largeFont = pygame.font.SysFont('comicsans', 60)
                            pausetext = largeFont.render('Pause', 1, (70, 70, 70))
                            win.blit(pausetext, (W / 2 - pausetext.get_width() / 2, H / 2 - pausetext.get_height()))
                            pygame.display.update()

                    def redrawWindow():
                        largeFont = pygame.font.SysFont('comicsans', 30)
                        win.blit(bg, (bgX, 0))
                        win.blit(bg, (bgX2, 0))
                        text = largeFont.render('Score: ' + str(score), 1, (70, 70, 70))
                        text1 = largeFont.render('HI: ' + str(updateFile()), 1, (70, 70, 70))
                        runner.draw(win)
                        for obstacle in obstacles:
                            obstacle.draw(win)
                        win.blit(text, (10, 10))
                        win.blit(text1, (W - text1.get_width() - 10, 10))
                        Button.draw(win)
                        pygame.display.update()

                    pygame.time.set_timer(USEREVENT + 1, 1000)
                    obstacles_event = pygame.USEREVENT
                    pygame.time.set_timer(obstacles_event + 1, 1200)
                    obstacles_event2 = pygame.USEREVENT
                    pygame.time.set_timer(obstacles_event2 + 2, 800)

                    speed = 60

                    score = 0
                    cookie_event = pygame.USEREVENT
                    pygame.time.set_timer(cookie_event, 175)

                    runner = player(200, 410, 64, 64)
                    Button = button1((70, 70, 70), 10, 40, 50, 25, 'Sound')
                    obstacles = []

                    while run:
                        for obstacle in obstacles:
                            if obstacle.collide(runner.hitbox):
                                runner.falling = True
                                lose_sound = mixer.Sound('images/bump.ogg')
                                if not Button.text == 'Silent':
                                    lose_sound.play()
                                endScreen()
                                speed = 60
                                score = 0
                                obstacles = []
                            if obstacle.x < -64:
                                obstacles.pop(obstacles.index(obstacle))
                            else:
                                obstacle.x -= 7.2

                        bgX -= 7
                        bgX2 -= 7
                        if bgX < bg.get_width() * -1:
                            bgX = bg.get_width()
                        if bgX2 < bg.get_width() * -1:
                            bgX2 = bg.get_width()

                        for event in pygame.event.get():
                            pos = pygame.mouse.get_pos()
                            keys = pygame.key.get_pressed()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                run = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    pauseScreen()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if Button.isOver(pos):
                                    if Button.text == 'Sound':
                                        Button.text = 'Silent'
                                    else:
                                        Button.text = 'Sound'

                            if event.type == pygame.MOUSEMOTION:
                                if Button.isOver(pos):
                                    Button.color = (50, 50, 50)
                                else:
                                    Button.color = (70, 70, 70)

                            if event.type == USEREVENT + 1:
                                speed += 1
                            if event.type == cookie_event:
                                score += 1

                            if event.type == obstacles_event + 1 and speed < 100:
                                r = random.randrange(0, 4)
                                if r == 0:
                                    obstacles.append(tree(810, 400, 48, 310))
                                elif r == 1:
                                    obstacles.append(SecondTree(810, 390, 48, 310))
                                elif r == 2:
                                    obstacles.append(eagle(810, 355, 64, 64))
                                elif r == 3:
                                    obstacles.append(eagle(810, 400, 64, 64))
                            if event.type == obstacles_event2 + 2 and speed >= 100:
                                r = random.randrange(0, 4)
                                if r == 0:
                                    obstacles.append(tree(810, 400, 48, 310))
                                elif r == 1:
                                    obstacles.append(SecondTree(810, 390, 48, 310))
                                elif r == 2:
                                    obstacles.append(eagle(810, 355, 64, 64))
                                elif r == 3:
                                    obstacles.append(eagle(810, 400, 64, 64))
                        if not runner.falling:
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                                if not runner.jumping:
                                    runner.jumping = True
                                    jump_sound = mixer.Sound('images/kick.ogg')
                                    if not Button.text == 'Silent':
                                        jump_sound.play()

                            if keys[pygame.K_DOWN]:
                                if not runner.sliding or not runner.jumping:
                                    runner.sliding = True

                        clock.tick(speed)
                        redrawWindow()




def main():
    enterWindow()

if __name__ == "__main__":
    pygame.init()
    
    main()

