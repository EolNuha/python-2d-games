import pygame
import math
import random
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('photos/background2.png')

# background sound
mixer.music.load('photos/background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('photos/cyclops.png')
pygame.display.set_icon(icon)

# explosion
explosionimg = pygame.image.load('photos/flame.png')

impactimg = pygame.image.load('photos/explosion.png')

player_shield = 150

rocket_shield = 150

boss_shield = 1500

boss1_shield = 5000

bossimg = pygame.image.load('photos/monster.png')
bossX = 370
bossY = 80
bossX_change = 3
bossY_change = 0

bossimg1 = pygame.image.load('photos/monster1.png')
boss1X = 0
boss1Y = 0
boss1X_change = 4.5
boss1Y_change = 2

# Level count
level_count = 1
level_countX = 350
level_countY = 10

# player
playerimg = pygame.image.load('photos/player3.png')
playerX = 370
playerY = 480
playerX_change = 0

# upgarde
upgradeimg = pygame.image.load('photos/player2.png')
upgradeX = 370
upgradeY = 480
upgradeX_change = 0

# level
levelimg = pygame.image.load('photos/player.png')
levelX = 370
levelY = 480
levelX_change = 0

# final
finalimg = pygame.image.load('photos/rocket (1).png')
finalX = 370
finalY = 480
finalX_change = 0

# rocketship
rocketshipimg = pygame.image.load('photos/rocket-ship.png')
rocketshipX = 370
rocketshipY = 480
rocketshipX_change = 0

bombimg = pygame.image.load('photos/bomb.png')
bombX = bossX
bombY = bossY
bombX_change = 0
bombY_change = 0

bomb1img = pygame.image.load('photos/bomb1.png')
bomb1X = bossX
bomb1Y = bossY
bomb1X_change = 0
bomb1Y_change = 0

# asteroid
asteroidimg = pygame.image.load('photos/asteroid.png')
asteroidX = random.randint(0, 715)
asteroidY = random.randint(0, 0)
asteroidX_change = 0
asteroidY_change = 0

# meteor
meteorimg = pygame.image.load('photos/asteroid (1).png')
meteorX = random.randint(0, 715)
meteorY = random.randint(0, 0)
meteorX_change = 0
meteorY_change = 0

# fall
fallimg = pygame.image.load('photos/asteroid (2).png')
fallX = random.randint(0, 715)
fallY = random.randint(0, 0)
fallX_change = 0
fallY_change = 0

# rock
rockimg = pygame.image.load('photos/meteor.png')
rockX = random.randint(200, 715)
rockY = random.randint(0, 0)
rockX_change = 0
rockY_change = 0

rockimg1 = pygame.image.load('photos/meteor.png')
rock1X = random.randint(0, 500)
rock1Y = random.randint(0, 0)
rock1X_change = 0
rock1Y_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('photos/alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(35)

# alien
alienimg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 2

for i in range(num_of_aliens):
    alienimg.append(pygame.image.load('photos/enemy.png'))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(100, 150))
    alienX_change.append(3.2)
    alienY_change.append(30)

# ufo
ufoimg = []
ufoX = []
ufoY = []
ufoX_change = []
ufoY_change = []
num_of_ufos = 3

for i in range(num_of_ufos):
    ufoimg.append(pygame.image.load('photos/ufo.png'))
    ufoX.append(random.randint(0, 736))
    ufoY.append(random.randint(100, 150))
    ufoX_change.append(3.5)
    ufoY_change.append(35)

# terror
terrorimg = []
terrorX = []
terrorY = []
terrorX_change = []
terrorY_change = []
num_of_terrors = 5

for i in range(num_of_terrors):
    terrorimg.append(pygame.image.load('photos/terror.png'))
    terrorX.append(random.randint(0, 736))
    terrorY.append(random.randint(-150, -10))
    terrorY_change.append(3)
    terrorX_change.append(0)

# bullet
bulletimg = pygame.image.load('photos/bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 6
# ready - you cant see the bullet on the screen until its fired
bullet_state = "ready"

bulletimg1 = pygame.image.load('photos/bullet.png')
bullet1X = 0
bullet1Y = playerY
bullet1X_change = 0
bullet1Y_change = 6
# ready - you cant see the bullet on the screen until its fired
bullet_state1 = "ready"

bulletimg2 = pygame.image.load('photos/bullet.png')
bullet2X = 0
bullet2Y = playerY
bullet2X_change = 0
bullet2Y_change = 6
# ready - you cant see the bullet on the screen until its fired
bullet_state2 = "ready"

bulletimg3 = pygame.image.load('photos/nuclear-bomb.png')
bullet3X = 0
bullet3Y = finalY
bullet3X_change = 0
bullet3Y_change = 7
# ready - you cant see the bullet on the screen until its fired
bullet_state3 = "ready"

missileimg = pygame.image.load('photos/missile.png')
missileX = 0
missileY = rocketshipY
missileX_change = 0
missileY_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state = "ready"

missileimg1 = pygame.image.load('photos/missile.png')
missile1X = 0
missile1Y = rocketshipY
missile1X_change = 0
missile1Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state1 = "ready"

missileimg2 = pygame.image.load('photos/missile.png')
missile2X = 0
missile2Y = rocketshipY
missile2X_change = 0
missile2Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state2 = "ready"

missileimg3 = pygame.image.load('photos/missile.png')
missile3X = 0
missile3Y = rocketshipY
missile3X_change = 0
missile3Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state3 = "ready"

missileimg4 = pygame.image.load('photos/missile.png')
missile4X = 0
missile4Y = rocketshipY
missile4X_change = 0
missile4Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state4 = "ready"

missileimg5 = pygame.image.load('photos/missile.png')
missile5X = 0
missile5Y = rocketshipY
missile5X_change = 0
missile5Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state5 = "ready"

missileimg6 = pygame.image.load('photos/missile.png')
missile6X = 0
missile6Y = rocketshipY
missile6X_change = 0
missile6Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state6 = "ready"

missileimg7 = pygame.image.load('photos/missile.png')
missile7X = 0
missile7Y = rocketshipY
missile7X_change = 0
missile7Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state7 = "ready"

missileimg8 = pygame.image.load('photos/missile.png')
missile8X = 0
missile8Y = rocketshipY
missile8X_change = 0
missile8Y_change = 10
# ready - you cant see the bullet on the screen until its fired
missile_state8 = "ready"

# Score
score_value = 0
font = pygame.font.Font('photos/Bruzh.otf', 32)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('photos/Bruzh.otf', 100)

# victory text
victory_font = pygame.font.Font('photos/Bruzh.otf', 100)

# player life
player_life_count = 3
player_font = pygame.font.Font('photos/Bruzh.otf', 32)
lifeX = 680
lifeY = 10


def shield_bar(surface, player_shield):
    if player_shield > 100:
        player_shield_color = (0, 255, 0)
    elif player_shield > 74:
        player_shield_color = (255, 255, 0)
    elif player_shield > 50:
        player_shield_color = (255, 150, 0)
    elif player_shield <= 50:
        player_shield_color = (255, 0, 0)

    pygame.draw.rect(screen, player_shield_color, (playerX - 20, playerY + 80, 100, 10))


def rocket_shield_bar(surface, rocket_shield):
    if rocket_shield > 140:
        rocket_shield_color = (0, 255, 0)
    elif rocket_shield > 130:
        rocket_shield_color = (50, 255, 0)
    elif rocket_shield > 120:
        rocket_shield_color = (80, 255, 0)
    elif rocket_shield > 110:
        rocket_shield_color = (120, 255, 0)
    elif rocket_shield > 100:
        rocket_shield_color = (170, 255, 0)
    elif rocket_shield > 85:
        rocket_shield_color = (210, 255, 0)
    elif rocket_shield > 75:
        rocket_shield_color = (255, 255, 0)
    elif rocket_shield > 65:
        rocket_shield_color = (255, 210, 0)
    elif rocket_shield > 55:
        rocket_shield_color = (255, 180, 0)
    elif rocket_shield > 40:
        rocket_shield_color = (255, 140, 0)
    elif rocket_shield > 25:
        rocket_shield_color = (255, 110, 0)
    elif rocket_shield > 10:
        rocket_shield_color = (255, 70, 0)
    elif rocket_shield <= 10:
        rocket_shield_color = (255, 0, 0)

    pygame.draw.rect(screen, rocket_shield_color, (rocketshipX - 20, rocketshipY + 80, 100, 10))


def boss_shield_bar(surface, boss_shield):
    if boss_shield > 1400:
        boss_shield_color = (0, 255, 0)
    elif boss_shield > 1300:
        boss_shield_color = (50, 255, 0)
    elif boss_shield > 1200:
        boss_shield_color = (80, 255, 0)
    elif boss_shield > 1100:
        boss_shield_color = (120, 255, 0)
    elif boss_shield > 1000:
        boss_shield_color = (170, 255, 0)
    elif boss_shield > 850:
        boss_shield_color = (210, 255, 0)
    elif boss_shield > 750:
        boss_shield_color = (255, 255, 0)
    elif boss_shield > 650:
        boss_shield_color = (255, 210, 0)
    elif boss_shield > 550:
        boss_shield_color = (255, 180, 0)
    elif boss_shield > 400:
        boss_shield_color = (255, 140, 0)
    elif boss_shield > 250:
        boss_shield_color = (255, 110, 0)
    elif boss_shield > 150:
        boss_shield_color = (255, 70, 0)
    elif boss_shield > 50:
        boss_shield_color = (255, 40, 0)
    elif boss_shield <= 50:
        boss_shield_color = (255, 0, 0)
    pygame.draw.rect(screen, boss_shield_color, (bossX - 35, bossY - 20, 200, 10))


def boss1_shield_bar(surface, boss1_shield):
    if boss1_shield > 4400:
        boss1_shield_color = (0, 255, 0)
    if boss1_shield > 4300:
        boss1_shield_color = (20, 255, 0)
    if boss1_shield > 4200:
        boss1_shield_color = (40, 255, 0)
    elif boss1_shield > 3900:
        boss1_shield_color = (50, 255, 0)
    elif boss1_shield > 3600:
        boss1_shield_color = (80, 255, 0)
    elif boss1_shield > 3300:
        boss1_shield_color = (120, 255, 0)
    elif boss1_shield > 3000:
        boss1_shield_color = (170, 255, 0)
    elif boss1_shield > 2700:
        boss1_shield_color = (210, 255, 0)
    elif boss1_shield > 2400:
        boss1_shield_color = (255, 255, 0)
    elif boss1_shield > 2100:
        boss1_shield_color = (255, 210, 0)
    elif boss1_shield > 1800:
        boss1_shield_color = (255, 180, 0)
    elif boss1_shield > 1500:
        boss1_shield_color = (255, 150, 0)
    elif boss1_shield > 1200:
        boss1_shield_color = (255, 120, 0)
    elif boss1_shield > 900:
        boss1_shield_color = (255, 85, 0)
    elif boss1_shield > 600:
        boss1_shield_color = (255, 50, 0)
    elif boss1_shield > 300:
        boss1_shield_color = (255, 30, 0)
    elif boss1_shield <= 300:
        boss1_shield_color = (255, 0, 0)
    pygame.draw.rect(screen, boss1_shield_color, (boss1X - 35, boss1Y - 20, 200, 10))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_life(x, y):
    hearts = font.render("Hearts: " + str(player_life_count), True, (255, 10, 10))
    screen.blit(hearts, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    over_text1 = over_font.render("Score: " + str(score_value), True, (255, 0, 0))
    screen.blit(over_text, (220, 210))
    screen.blit(over_text1, (220, 310))


def restart():
    over_text3 = font.render("Press SPACE to play again", True, (0, 0, 0))
    screen.blit(over_text3, (220, 410))


def forward():
    over_text4 = font.render("Press SPACE to continue", True, (0, 0, 0))
    screen.blit(over_text4, (220, 410))


def victory_text():
    game_text = over_font.render("VICTORY", True, (255, 255, 255))
    screen.blit(game_text, (250, 200))


def level_up():
    level_up = font.render("LEVEL UP", True, (255, 255, 255))
    screen.blit(level_up, (350, 570))


def next_level(x, y):
    next_level = font.render("Level: " + str(level_count), True, (255, 255, 255))
    screen.blit(next_level, (x, y))


def boss(x, y):
    screen.blit(bossimg, (x, y))


def boss1(x, y):
    screen.blit(bossimg1, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def rocketship(x, y):
    screen.blit(rocketshipimg, (x, y))


def bomb(x, y):
    screen.blit(bombimg, (x, y))


def bomb1(x, y):
    screen.blit(bomb1img, (x, y))


def asteroid(x, y):
    screen.blit(asteroidimg, (x, y))


def meteor(x, y):
    screen.blit(meteorimg, (x, y))


def fall(x, y):
    screen.blit(fallimg, (x, y))


def rock(x, y):
    screen.blit(rockimg, (x, y))


def rock1(x, y):
    screen.blit(rockimg1, (x, y))


def upgrade(x, y):
    screen.blit(upgradeimg, (x, y))


def level(x, y):
    screen.blit(levelimg, (x, y))


def final(x, y):
    screen.blit(finalimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def terror(x, y, i):
    screen.blit(terrorimg[i], (x, y))


def alien(x, y, i):
    screen.blit(alienimg[i], (x, y))


def ufo(x, y, i):
    screen.blit(ufoimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def fire_bullet1(x, y):
    global bullet_state1
    bullet_state1 = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def fire_bullet2(x, y):
    global bullet_state2
    bullet_state2 = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def fire_bullet3(x, y):
    global bullet_state3
    bullet_state3 = "fire"
    screen.blit(bulletimg3, (x + 16, y + 10))


def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileimg, (x + 16, y + 10))


def fire_missile1(x, y):
    global missile_state1
    missile_state1 = "fire"
    screen.blit(missileimg1, (x + 16, y + 10))


def fire_missile2(x, y):
    global missile_state2
    missile_state2 = "fire"
    screen.blit(missileimg2, (x - 10, y + 10))


def fire_missile3(x, y):
    global missile_state3
    missile_state3 = "fire"
    screen.blit(missileimg3, (x + 16, y + 10))


def fire_missile4(x, y):
    global missile_state4
    missile_state4 = "fire"
    screen.blit(missileimg4, (x - 10, y + 10))


def fire_missile5(x, y):
    global missile_state5
    missile_state5 = "fire"
    screen.blit(missileimg5, (x - 10, y + 10))


def fire_missile6(x, y):
    global missile_state6
    missile_state6 = "fire"
    screen.blit(missileimg6, (x + 42, y + 10))


def fire_missile7(x, y):
    global missile_state7
    missile_state7 = "fire"
    screen.blit(missileimg7, (x + 42, y + 10))


def fire_missile8(x, y):
    global missile_state8
    missile_state8 = "fire"
    screen.blit(missileimg8, (x + 42, y + 10))


def terrorimpact(terrorX, terrorY, missileX, missileY):
    distance = math.sqrt(math.pow(((terrorX + 8) - missileX), 2) + math.pow((terrorY - missileY), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorimpact1(terrorX, terrorY, missile1X, missile1Y):
    distance = math.sqrt(math.pow(((terrorX + 8) - missile1X), 2) + math.pow((terrorY - missile1Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorimpact2(terrorX, terrorY, missile2X, missile2Y):
    distance = math.sqrt(math.pow(((terrorX + 8) - missile2X), 2) + math.pow((terrorY - missile2Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorimpact3(terrorX, terrorY, missile3X, missile3Y):
    distance = math.sqrt(math.pow(((terrorX + 8) - missile3X), 2) + math.pow((terrorY - missile3Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorimpact4(terrorX, terrorY, missile4X, missile4Y):
    distance = math.sqrt(math.pow(((terrorX + 8) - missile4X), 2) + math.pow((terrorY - missile4Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorimpact5(terrorX, terrorY, missile5X, missile5Y):
    distance = math.sqrt(math.pow(((terrorX + 8) - missile5X), 2) + math.pow((terrorY - missile5Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def boss1impact6(boss1X, boss1Y, missile6X, missile6Y):
    distance = math.sqrt(math.pow(((boss1X + 50) - missile6X), 2) + math.pow(((boss1Y + 50) - missile6Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact(boss1X, boss1Y, missileX, missileY):
    distance = math.sqrt(math.pow(((boss1X + 50) - missileX), 2) + math.pow(((boss1Y + 50) - missileY), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact1(boss1X, boss1Y, missile1X, missile1Y):
    distance = math.sqrt(math.pow(((boss1X + 50) - missile1X), 2) + math.pow(((boss1Y + 50) - missile1Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact2(boss1X, boss1Y, missile2X, missile2Y):
    distance = math.sqrt(math.pow((boss1X - missile2X), 2) + math.pow((boss1Y - missile2Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact3(boss1X, boss1Y, missile3X, missile3Y):
    distance = math.sqrt(math.pow(((boss1X + 50) - missile3X), 2) + math.pow(((boss1Y + 50) - missile3Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact4(boss1X, boss1Y, missile4X, missile4Y):
    distance = math.sqrt(math.pow((boss1X - missile4X), 2) + math.pow((boss1Y - missile4Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact5(boss1X, boss1Y, missile5X, missile5Y):
    distance = math.sqrt(math.pow((boss1X - missile5X), 2) + math.pow((boss1Y - missile5Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact7(boss1X, boss1Y, missile7X, missile7Y):
    distance = math.sqrt(math.pow(((boss1X + 50) - missile7X), 2) + math.pow(((boss1Y + 50) - missile7Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def boss1impact8(boss1X, boss1Y, missile8X, missile8Y):
    distance = math.sqrt(math.pow(((boss1X + 50) - missile8X), 2) + math.pow(((boss1Y + 50) - missile8Y), 2))
    if distance <= 50:
        return True
    else:
        return False


def rocketboss(boss1X, boss1Y, rocketshipX, rocketshipY):
    distance = math.sqrt(math.pow(((boss1X + 50) - rocketshipX), 2) + math.pow(((boss1Y + 50) - rocketshipY), 2))
    if distance <= 50:
        return True
    else:
        return False


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(((enemyX + 8) - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance <= 30:
        return True
    else:
        return False


def isCollision1(enemyX, enemyY, bullet1X, bullet1Y):
    distance = math.sqrt(math.pow(((enemyX + 8) - bullet1X), 2) + math.pow((enemyY - bullet1Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def isCollision2(enemyX, enemyY, bullet2X, bullet2Y):
    distance = math.sqrt(math.pow(((enemyX + 8) - bullet2X), 2) + math.pow((enemyY - bullet2Y), 2))
    if distance <= 30:
        return True
    else:
        return False


def alienCollision(alienX, alienY, bulletX, bulletY):
    far = math.sqrt(math.pow(((alienX + 8) - bulletX), 2) + math.pow((alienY - bulletY), 2))
    if far <= 30:
        return True
    else:
        return False


def alienCollision1(alienX, alienY, bullet1X, bullet1Y):
    far = math.sqrt(math.pow(((alienX + 8) - bullet1X), 2) + math.pow((alienY - bullet1Y), 2))
    if far <= 30:
        return True
    else:
        return False


def alienCollision2(alienX, alienY, bullet2X, bullet2Y):
    far = math.sqrt(math.pow(((alienX + 8) - bullet2X), 2) + math.pow((alienY - bullet2Y), 2))
    if far <= 30:
        return True
    else:
        return False


def ufoCollision(ufoX, ufoY, bulletX, bulletY):
    close = math.sqrt(math.pow(((ufoX + 8) - bulletX), 2) + math.pow((ufoY - bulletY), 2))
    if close <= 30:
        return True
    else:
        return False


def ufoCollision1(ufoX, ufoY, bullet1X, bullet1Y):
    close = math.sqrt(math.pow(((ufoX + 8) - bullet1X), 2) + math.pow((ufoY - bullet1Y), 2))
    if close <= 30:
        return True
    else:
        return False


def ufoCollision2(ufoX, ufoY, bullet2X, bullet2Y):
    close = math.sqrt(math.pow(((ufoX + 8) - bullet2X), 2) + math.pow((ufoY - bullet2Y), 2))
    if close <= 30:
        return True
    else:
        return False


def asteroidCollision(asteroidX, asteroidY, playerX, playerY):
    close = math.sqrt(math.pow((((asteroidX + 8) - 10) - playerX), 2) + math.pow(((asteroidY + 15) - playerY), 2))
    if close < 43:
        return True
    else:
        return False


def meteorCollision(meteorX, meteorY, playerX, playerY):
    close = math.sqrt(math.pow((((meteorX + 8) - 10) - playerX), 2) + math.pow(((meteorY + 15) - playerY), 2))
    if close < 43:
        return True
    else:
        return False


def fallCollision(fallX, fallY, playerX, playerY):
    close = math.sqrt(math.pow((((fallX + 8) - 10) - playerX), 2) + math.pow(((fallY + 15) - playerY), 2))
    if close < 43:
        return True
    else:
        return False


def rockCollision(rockX, rockY, rocketshipX, rocketshipY):
    close = math.sqrt(math.pow((((rockX + 8) - 10) - rocketshipX), 2) + math.pow(((rockY + 15) - rocketshipY), 2))
    if close < 43:
        return True
    else:
        return False


def rock1Collision(rock1X, rock1Y, rocketshipX, rocketshipY):
    close = math.sqrt(math.pow((((rock1X + 8) - 10) - rocketshipX), 2) + math.pow(((rock1Y + 15) - rocketshipY), 2))
    if close < 43:
        return True
    else:
        return False


def enemyCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow((enemyX - playerX), 2) + math.pow((enemyY - playerY + 8), 2))
    if distance <= 30:
        return True
    else:
        return False


def alien_playerCollision(alienX, alienY, playerX, playerY):
    distance = math.sqrt(math.pow((alienX - playerX), 2) + math.pow((alienY - playerY + 8), 2))
    if distance <= 30:
        return True
    else:
        return False


def ufo_playerCollision(ufoX, ufoY, playerX, playerY):
    distance = math.sqrt(math.pow((ufoX - playerX), 2) + math.pow((ufoY - playerY + 8), 2))
    if distance <= 30:
        return True
    else:
        return False


def terrorCollision(terrorX, terrorY, rocketshipX, rocketshipY):
    distance = math.sqrt(math.pow((terrorX - rocketshipX), 2) + math.pow((terrorY - rocketshipY + 8), 2))
    if distance <= 30:
        return True
    else:
        return False


def bossCollision(bossX, bossY, bullet3X, bullet3Y):
    close = math.sqrt(math.pow(((bossX + 50) - bullet3X), 2) + math.pow(((bossY + 50) - bullet3Y), 2))
    if close <= 50:
        return True
    else:
        return False


def finalCollision(bombX, bombY, playerX, playerY):
    distance = math.sqrt(math.pow((bombX - playerX), 2) + math.pow((bombY - playerY), 2))
    if distance <= 30:
        return True
    else:
        return False


def roundCollision(bomb1X, bomb1Y, rocketshipX, rocketshipY):
    distance = math.sqrt(math.pow((bomb1X - rocketshipX), 2) + math.pow((bomb1Y - rocketshipY), 2))
    if distance <= 100:
        return True
    else:
        return False


# Game Loop - which means that the game window is always running until the close button is pressed
running = True
while running:
    # RGB - red green blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed , check wether is left or right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -4
                upgradeX_change = -4
                levelX_change = -4
                finalX_change = -4
                rocketshipX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
                upgradeX_change = 4
                levelX_change = 4
                finalX_change = 4
                rocketshipX_change = 4
            if event.key == pygame.K_SPACE and bullet_state == "ready" and score_value < 100:
                bullet_Sound = mixer.Sound('photos/laser.wav')
                bullet_Sound.play()
                # Get the current coordinates of player x
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_SPACE and bullet_state1 == "ready" and score_value < 100 and bulletY <= 350:
                bullet_Sound1 = mixer.Sound('photos/laser.wav')
                bullet_Sound1.play()
                # Get the current coordinates of player x
                bullet1X = playerX
                bullet1Y = playerY
                fire_bullet1(bullet1X, bullet1Y)
            if event.key == pygame.K_SPACE and bullet_state2 == "ready" and score_value < 100 and bullet1Y <= 350:
                bullet_Sound2 = mixer.Sound('photos/laser.wav')
                bullet_Sound2.play()
                # Get the current coordinates of player x
                bullet2X = playerX
                bullet2Y = playerY
                fire_bullet2(bullet2X, bullet2Y)
            if event.key == pygame.K_SPACE and bullet_state3 == "ready" and score_value == 100 and boss_shield > 0:
                bullet_Sound3 = mixer.Sound('photos/laser.wav')
                bullet_Sound3.play()
                # Get the current coordinates of player x
                bullet3X = playerX
                bullet3Y = playerY
                fire_bullet3(bullet3X, bullet3Y)
            if event.key == pygame.K_SPACE and missile_state == "ready" and score_value > 100:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missileX = rocketshipX
                missileY = rocketshipY
                fire_missile(missileX, missileY)
            if event.key == pygame.K_SPACE and missile_state1 == "ready" and score_value >= 100 and missileY <= 400 and missile3Y <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile1X = rocketshipX
                missile1Y = rocketshipY
                fire_missile1(missile1X, missile1Y)
            if event.key == pygame.K_SPACE and missile_state2 == "ready" and score_value >= 100:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile2X = rocketshipX
                missile2Y = rocketshipY
                fire_missile2(missile2X, missile2Y)
            if event.key == pygame.K_SPACE and missile_state3 == "ready" and score_value > 100 and missileY <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile3X = rocketshipX
                missile3Y = rocketshipY
                fire_missile3(missile3X, missile3Y)
            if event.key == pygame.K_SPACE and missile_state4 == "ready" and score_value >= 100 and missile2Y <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile4X = rocketshipX
                missile4Y = rocketshipY
                fire_missile4(missile4X, missile4Y)
            if event.key == pygame.K_SPACE and missile_state5 == "ready" and score_value >= 100 and missile2Y <= 400 and missile4Y <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile5X = rocketshipX
                missile5Y = rocketshipY
                fire_missile5(missile5X, missile5Y)
            if event.key == pygame.K_SPACE and missile_state6 == "ready" and score_value >= 100:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile6X = rocketshipX
                missile6Y = rocketshipY
                fire_missile6(missile6X, missile6Y)
            if event.key == pygame.K_SPACE and missile_state7 == "ready" and score_value >= 100 and missile6Y <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile7X = rocketshipX
                missile7Y = rocketshipY
                fire_missile7(missile7X, missile7Y)
            if event.key == pygame.K_SPACE and missile_state8 == "ready" and score_value >= 100 and missile6Y <= 400 and missile7Y <= 450:
                missile_Sound = mixer.Sound('photos/laser.wav')
                missile_Sound.play()
                # Get the current coordinates of player x
                missile8X = rocketshipX
                missile8Y = rocketshipY
                fire_missile8(missile8X, missile8Y)

            if event.key == pygame.K_SPACE and player_life_count <= 0 and score_value <= 100:
                upgradeY = 480
                levelY = 480
                player_life_count = 3
                player_shield = 150
                boss_shield = 1500
                for i in range(num_of_enemies):
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
                for i in range(num_of_aliens):
                    alienX[i] = random.randint(0, 736)
                    alienY[i] = random.randint(50, 150)
                for i in range(num_of_ufos):
                    ufoX[i] = random.randint(0, 736)
                    ufoY[i] = random.randint(50, 150)
                level_count = 1
                score_value = 0
                fallX = random.randint(0, 730)
                fallY = random.randint(0, 0)
                meteorX = random.randint(0, 730)
                meteorY = random.randint(0, 0)
                asteroidX = random.randint(0, 730)
                asteroidY = random.randint(0, 0)
                bossX = 370
                bossY = 80

            if event.key == pygame.K_SPACE and player_life_count <= 0 and score_value >= 101:
                score_value = 101
                level_count = 4
                rocketshipY = 480
                player_life_count = 3
                rocket_shield = 150
                for i in range(num_of_terrors):
                    terrorX[i] = random.randint(0, 736)
                    terrorY[i] = random.randint(-150, -10)
                boss1X_change = 2
                boss1Y_change = 4.5
                boss1X = 0
                boss1Y = 0
                boss1_shield = 5000

            if event.key == pygame.K_SPACE and boss_shield <= 0 and score_value == 100:
                score_value = 101
                player_life_count = 3
            if event.key == pygame.K_SPACE and boss1_shield <= 0 and score_value == 350:
                score_value = 351
                player_life_count = 5
                rocket_shield = 150
                for i in range(num_of_terrors):
                    terrorX[i] = random.randint(0, 736)
                    terrorY[i] = random.randint(-150, -10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                upgradeX_change = 0
                levelX_change = 0
                finalX_change = 0
                rocketshipX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                upgradeX_change = 0
                levelX_change = 0
                finalX_change = 0
                rocketshipX_change = 0

    # checking for boundries so it doesnt go out of bounds
    playerX += playerX_change

    upgradeX += upgradeX_change

    levelX += levelX_change

    finalX += finalX_change

    rocketshipX += rocketshipX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if levelX <= 0:
        levelX = 0
    elif levelX >= 736:
        levelX = 736

    if upgradeX <= 0:
        upgradeX = 0
    elif upgradeX >= 736:
        upgradeX = 736

    if finalX <= 0:
        finalX = 0
    elif finalX >= 736:
        finalX = 736

    if rocketshipX <= 0:
        rocketshipX = 0
    elif rocketshipX >= 736:
        rocketshipX = 736

    fallY += fallY_change
    if fallY >= 0:
        fallY_change = 5

    if fallY == 850:
        fallX = random.randint(0, 730)
        fallY = random.randint(0, 0)

    meteorcollision3 = fallCollision(fallX, fallY, playerX, playerY)
    if meteorcollision3:
        player_shield -= 50
        screen.blit(explosionimg, (playerX, playerY))
        boom = mixer.Sound('photos/earthquake.wav')
        boom.play()
        fallX = random.randint(0, 730)
        fallY = random.randint(0, 0)
        if player_shield <= 0:
            player_life_count += -1
            fallX = random.randint(0, 730)
            fallY = random.randint(0, 0)
            if player_life_count == 2:
                player_shield = 150
                fallX = random.randint(0, 730)
                fallY = random.randint(0, 0)
            if player_life_count == 1:
                player_shield = 150
                fallX = random.randint(0, 730)
                fallY = random.randint(0, 0)

    fall(fallX, fallY)

    if player_life_count <= 0:
        for i in range(num_of_enemies):
            enemyY[i] = 2000
        playerX_change = 0
        upgradeX_change = 0
        levelX_change = 0
        finalX_change = 0
        asteroidY = 2000
        meteorY = 2000
        fallY = 2000
        bossY = 2000
        game_over_text()
        restart()

    for i in range(num_of_enemies):
        playercollision = enemyCollision(enemyX[i], enemyY[i], playerX, playerY)
        # Game Over
        if playercollision:
            explosion12 = mixer.Sound('photos/earthquake.wav')
            explosion12.play()
            player_shield -= 150
            if player_shield <= 0:
                player_life_count += -1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
                if player_life_count == 2:
                    player_shield = 150
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
                if player_life_count == 1:
                    player_shield = 150
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
        if player_life_count <= 0:
            for i in range(num_of_enemies):
                enemyY[i] = 2000
            playerX_change = 0
            upgradeX_change = 0
            levelX_change = 0
            finalX_change = 0
            asteroidY = 2000
            meteorY = 2000
            fallY = 2000
            game_over_text()
            restart()
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision and bullet_state == "fire":
            screen.blit(explosionimg, (enemyX[i], enemyY[i]))
            explosion = mixer.Sound('photos/explosion.wav')
            explosion.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        collision1 = isCollision1(enemyX[i], enemyY[i], bullet1X, bullet1Y)
        if collision1 and bullet_state1 == "fire":
            screen.blit(explosionimg, (enemyX[i], enemyY[i]))
            explosion1 = mixer.Sound('photos/explosion.wav')
            explosion1.play()
            bullet1Y = 480
            bullet_state1 = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        collision2 = isCollision2(enemyX[i], enemyY[i], bullet2X, bullet2Y)
        if collision2 and bullet_state2 == "fire":
            screen.blit(explosionimg, (enemyX[i], enemyY[i]))
            explosion2 = mixer.Sound('photos/explosion.wav')
            explosion2.play()
            bullet2Y = 480
            bullet_state2 = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if score_value < 25:
        player(playerX, playerY)
        shield_bar(screen, player_shield)

    if score_value >= 25:
        shield_bar(screen, player_shield)
        level_count = 2
        upgrade(upgradeX, upgradeY)
        if bullet1Y <= 0:
            bullet1Y = 480
            bullet_state1 = "ready"
        if bullet_state1 == "fire":
            fire_bullet1(bullet1X, bullet1Y)
            bullet1Y -= bullet1Y_change
        if score_value == 25:
            level_up()

        asteroidY += asteroidY_change
        asteroidX += asteroidX_change
        if asteroidY >= 0:
            asteroidY_change = 5
            asteroidX_change = 1

        if asteroidY == 1150:
            asteroidX = random.randint(0, 730)
            asteroidY = random.randint(0, 0)

        meteorcollision = asteroidCollision(asteroidX, asteroidY, playerX, playerY)
        if meteorcollision:
            player_shield -= 75
            screen.blit(explosionimg, (playerX, playerY))
            boom1 = mixer.Sound('photos/earthquake.wav')
            boom1.play()
            asteroidX = random.randint(0, 730)
            asteroidY = random.randint(0, 0)
            if player_shield <= 0:
                player_life_count += -1
                asteroidX = random.randint(0, 730)
                asteroidY = random.randint(0, 0)
                if player_life_count == 2:
                    player_shield = 150
                    asteroidX = random.randint(0, 730)
                    asteroidY = random.randint(0, 0)
                if player_life_count == 1:
                    player_shield = 150
                    asteroidX = random.randint(0, 730)
                    asteroidY = random.randint(0, 0)
        asteroid(asteroidX, asteroidY)

        for i in range(num_of_aliens):
            alienplayercollision = alien_playerCollision(alienX[i], alienY[i], playerX, playerY)
            # Game Over
            if alienplayercollision:
                explosion11 = mixer.Sound('photos/earthquake.wav')
                explosion11.play()
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)
                player_shield -= 150
                if player_shield <= 0:
                    player_life_count += -1
                    alienX[i] = random.randint(0, 736)
                    alienY[i] = random.randint(50, 150)
                    if player_life_count == 2:
                        player_shield = 150
                        alienX[i] = random.randint(0, 736)
                        alienY[i] = random.randint(50, 150)
                    if player_life_count == 1:
                        player_shield = 150
                        alienX[i] = random.randint(0, 736)
                        alienY[i] = random.randint(50, 150)
            if player_life_count <= 0:
                for i in range(num_of_aliens):
                    alienY[i] = 2000
                playerX_change = 0
                upgradeX_change = 0
                levelX_change = 0
                finalX_change = 0
                asteroidY = 2000
                meteorY = 2000
                fallY = 2000
                game_over_text()
                restart()
            alienX[i] += alienX_change[i]
            if alienX[i] <= 0:
                alienX_change[i] = 3
                alienY[i] += alienY_change[i]
            elif alienX[i] >= 736:
                alienX_change[i] = -3
                alienY[i] += alienY_change[i]

            # Collision
            collisionalien = alienCollision(alienX[i], alienY[i], bulletX, bulletY)
            if collisionalien and bullet_state == "fire":
                screen.blit(explosionimg, (alienX[i], alienY[i]))
                explosion3 = mixer.Sound('photos/explosion.wav')
                explosion3.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)

            alien(alienX[i], alienY[i], i)

            collisionalien1 = alienCollision1(alienX[i], alienY[i], bullet1X, bullet1Y)
            if collisionalien1 and bullet_state1 == "fire":
                screen.blit(explosionimg, (alienX[i], alienY[i]))
                explosion4 = mixer.Sound('photos/explosion.wav')
                explosion4.play()
                bullet1Y = 480
                bullet_state1 = "ready"
                score_value += 1
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)

            alien(alienX[i], alienY[i], i)

            collisionalien2 = alienCollision2(alienX[i], alienY[i], bullet2X, bullet2Y)
            if collisionalien2 and bullet_state2 == "fire":
                screen.blit(explosionimg, (alienX[i], alienY[i]))
                explosion5 = mixer.Sound('photos/explosion.wav')
                explosion5.play()
                bullet2Y = 480
                bullet_state2 = "ready"
                score_value += 1
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)

            alien(alienX[i], alienY[i], i)

    if score_value >= 50:
        shield_bar(screen, player_shield)
        upgradeY = 2000
        level_count = 3
        level(levelX, levelY)
        if bullet2Y <= 0:
            bullet2Y = 480
            bullet_state2 = "ready"
        if bullet_state2 == "fire":
            fire_bullet2(bullet2X, bullet2Y)
            bullet2Y -= bullet2Y_change
        if score_value == 50:
            level_up()

        meteorY += meteorY_change
        meteorX += meteorX_change
        if meteorY >= 0:
            meteorY_change = 7
            meteorX_change = -1

        if meteorY == 1001:
            meteorX = random.randint(0, 730)
            meteorY = random.randint(0, 0)

        meteorcollision1 = meteorCollision(meteorX, meteorY, playerX, playerY)
        if meteorcollision1:
            player_shield -= 75
            player_shield -= 50
            screen.blit(explosionimg, (playerX, playerY))
            boom2 = mixer.Sound('photos/earthquake.wav')
            boom2.play()
            meteorX = random.randint(0, 730)
            meteorY = random.randint(0, 0)
            if player_shield <= 0:
                player_life_count += -1
                meteorX = random.randint(0, 730)
                meteorY = random.randint(0, 0)
                if player_life_count == 2:
                    player_shield = 150
                    meteorX = random.randint(0, 730)
                    meteorY = random.randint(0, 0)
                if player_life_count == 1:
                    player_shield = 150
                    meteorX = random.randint(0, 730)
                    meteorY = random.randint(0, 0)
        meteor(meteorX, meteorY)

        for i in range(num_of_ufos):
            ufoplayercollision = ufo_playerCollision(ufoX[i], ufoY[i], playerX, playerY)
            # Game Over
            if ufoplayercollision:
                explosion10 = mixer.Sound('photos/earthquake.wav')
                explosion10.play()
                ufoX[i] = random.randint(0, 736)
                ufoY[i] = random.randint(50, 150)
                player_shield -= 150
                if player_shield <= 0:
                    player_life_count += -1
                    alienX[i] = random.randint(0, 736)
                    alienY[i] = random.randint(50, 150)
                    if player_life_count == 2:
                        player_shield = 150
                        alienX[i] = random.randint(0, 736)
                        alienY[i] = random.randint(50, 150)
                    if player_life_count == 1:
                        player_shield = 150
                        alienX[i] = random.randint(0, 736)
                        alienY[i] = random.randint(50, 150)
            if player_life_count <= 0:
                for i in range(num_of_ufos):
                    ufoY[i] = 2000
                playerX_change = 0
                upgradeX_change = 0
                levelX_change = 0
                finalX_change = 0
                asteroidY = 2000
                meteorY = 2000
                fallY = 2000
                game_over_text()
                restart()
            ufoX[i] += ufoX_change[i]
            if ufoX[i] <= 0:
                ufoX_change[i] = 3
                ufoY[i] += ufoY_change[i]
            elif ufoX[i] >= 736:
                ufoX_change[i] = -3
                ufoY[i] += ufoY_change[i]

            # Collision
            collisionufo = ufoCollision(ufoX[i], ufoY[i], bulletX, bulletY)
            if collisionufo and bullet_state == "fire":
                screen.blit(explosionimg, (ufoX[i], ufoY[i]))
                explosion6 = mixer.Sound('photos/explosion.wav')
                explosion6.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                ufoX[i] = random.randint(0, 736)
                ufoY[i] = random.randint(50, 150)

            ufo(ufoX[i], ufoY[i], i)

            collisionufo1 = ufoCollision1(ufoX[i], ufoY[i], bullet1X, bullet1Y)
            if collisionufo1 and bullet_state1 == "fire":
                screen.blit(explosionimg, (ufoX[i], ufoY[i]))
                explosion7 = mixer.Sound('photos/explosion.wav')
                explosion7.play()
                bullet1Y = 480
                bullet_state1 = "ready"
                score_value += 1
                ufoX[i] = random.randint(0, 736)
                ufoY[i] = random.randint(50, 150)

            ufo(ufoX[i], ufoY[i], i)

            collisionufo2 = ufoCollision2(ufoX[i], ufoY[i], bullet2X, bullet2Y)
            if collisionufo2 and bullet_state2 == "fire":
                screen.blit(explosionimg, (ufoX[i], ufoY[i]))
                explosion8 = mixer.Sound('photos/explosion.wav')
                explosion8.play()
                bullet2Y = 480
                bullet_state2 = "ready"
                score_value += 1
                ufoX[i] = random.randint(0, 736)
                ufoY[i] = random.randint(50, 150)

            ufo(ufoX[i], ufoY[i], i)

    if score_value == 100:
        shield_bar(screen, player_shield)
        levelY = 2000
        final(finalX, finalY)
        level_count = "Boss level"
        if bullet3Y <= 0:
            bullet3Y = 480
            bullet_state3 = "ready"
        if bullet_state3 == "fire":
            fire_bullet3(bullet3X, bullet3Y)
            bullet3Y -= bullet3Y_change
        boss(bossX, bossY)
        for i in range(num_of_ufos):
            ufoY[i] = 2000
        for i in range(num_of_aliens):
            alienY[i] = 2000
        for i in range(num_of_enemies):
            enemyY[i] = 2000

        bombY += bombY_change
        if bombY >= 0:
            bombY_change = 7

        if bombY == 801:
            bombX = bossX
            bombY = bossY
        bomb(bombX, bombY)

        bossX += bossX_change
        if bossX <= 0:
            bossX_change = 3.7
        if bossX >= 700:
            bossX_change = -3.7

        collisionboss = bossCollision(bossX, bossY, bullet3X, bullet3Y)
        if collisionboss and bullet_state3 == "fire":
            boss_shield -= 100
            screen.blit(explosionimg, (bossX, bossY))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            bullet3Y = 480
            bullet_state3 = "ready"

        boss(bossX, bossY)
        boss_shield_bar(screen, boss_shield)
        if boss_shield <= 0:
            bossY = 2000
            asteroidY = 2000
            fallY = 2000
            meteorY = 2000
            victory_text()
            forward()

        finalplayercollision = finalCollision(bombX, bombY, finalX, finalY)
        if finalplayercollision:
            player_shield -= 150
            screen.blit(impactimg, (finalX, finalY))
            boom2 = mixer.Sound('photos/earthquake.wav')
            boom2.play()
            bombX = bossX
            bombY = bossY
            if player_shield <= 0:
                player_life_count += -1
                bombX = random.randint(0, 730)
                asteroidY = random.randint(0, 0)
                if player_life_count == 2:
                    player_shield = 150
                    bombX = bossX
                    bombY = bossY
                if player_life_count == 1:
                    player_shield = 150
                    bombX = bossX
                    bombY = bossY
        bomb(bombX, bombY)

    if score_value >= 101:
        rocket_shield_bar(screen, rocket_shield)
        level_count = 4
        finalY = 2000
        rocketship(rocketshipX, rocketshipY)
        if missileY <= 0:
            missileY = rocketshipY
            missile_state = "ready"
        if missile_state == "fire":
            fire_missile(missileX, missileY)
            missileY -= missileY_change

        for i in range(num_of_terrors):
            playercollision = terrorCollision(terrorX[i], terrorY[i], rocketshipX, rocketshipY)
            # Game Over
            if playercollision:
                explosion12 = mixer.Sound('photos/earthquake.wav')
                explosion12.play()
                rocket_shield -= 150
                if rocket_shield <= 0:
                    player_life_count += -1
                    terrorX[i] = random.randint(0, 736)
                    terrorY[i] = random.randint(-150, -10)
                    if player_life_count == 2:
                        rocket_shield = 150
                        terrorX[i] = random.randint(0, 736)
                        terrorY[i] = random.randint(-150, -10)
                    if player_life_count == 1:
                        rocket_shield = 150
                        terrorX[i] = random.randint(0, 736)
                        terrorY[i] = random.randint(-150, -10)
            if player_life_count <= 0:
                player_life_count = 0
                for i in range(num_of_terrors):
                    terrorY[i] = -2000
                rockY = -2000
                rock1Y = -2000
                rocketshipX_change = 0
                boss1Y = 100
                boss1X = 380
                boss1X_change = 0
                boss1Y_change = 0
                game_over_text()
                restart()
            terrorY[i] += terrorY_change[i]
            if terrorY[i] >= -150:
                terrorY_change[i] = 3

            if terrorY[i] >= 650:
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)
            bomb(bombX, bombY)
            # Collision
            collision = terrorimpact(terrorX[i], terrorY[i], missileX, missileY)
            if collision and missile_state == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missileY = rocketshipY
                missile_state = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

            collision3 = terrorimpact3(terrorX[i], terrorY[i], missile3X, missile3Y)
            if collision3 and missile_state3 == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missile3Y = rocketshipY
                missile_state3 = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

            terror(terrorX[i], terrorY[i], i)

        # bullet movement

        if missile3Y <= 0:
            missile3Y = 480
            missile_state3 = "ready"
        if missile_state3 == "fire":
            fire_missile3(missile3X, missile3Y)
            missile3Y -= missile3Y_change

    if score_value >= 175:
        if score_value == 175:
            level_up()
            player_life_count = 3
            rocket_shield = 150
        level_count = 5
        if missile1Y <= 0:
            missile1Y = 480
            missile_state1 = "ready"
        if missile_state1 == "fire":
            fire_missile1(missile1X, missile1Y)
            missile1Y -= missile1Y_change
        for i in range(num_of_terrors):

            collisionimpact1 = terrorimpact1(terrorX[i], terrorY[i], missile1X, missile1Y)
            if collisionimpact1 and missile_state1 == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missile1Y = rocketshipY
                missile_state1 = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

            terror(terrorX[i], terrorY[i], i)

            terror(terrorX[i], terrorY[i], i)

            bomb1Y += bomb1Y_change
            if bomb1Y >= 0:
                bomb1Y_change = 3

            if bomb1Y >= 1000:
                bomb1X = terrorX[i] + 15
                bomb1Y = terrorY[i]
            bomb1(bomb1X, bomb1Y)

            roundrocketcollision = roundCollision(bomb1X, bomb1Y, rocketshipX, rocketshipY)
            if roundrocketcollision:
                rocket_shield -= 5
                bomb1X = terrorX[i] + 15
                bomb1Y = terrorY[i]
                if rocket_shield <= 0:
                    player_life_count += -1
                    if player_life_count == 2:
                        rocket_shield = 150
                        bomb1X = terrorX[i]
                        bomb1Y = terrorY[i]
                    if player_life_count == 1:
                        rocket_shield = 150
                        bomb1X = terrorX[i]
                        bomb1Y = terrorY[i]
            bomb1(bomb1X, bomb1Y)

    if score_value >= 250:
        if missile2Y <= 0:
            missile2Y = rocketshipY
            missile_state2 = "ready"
        if missile_state2 == "fire":
            fire_missile2(missile2X, missile2Y)
            missile2Y -= missile2Y_change

        if missile4Y <= 0:
            missile4Y = rocketshipY
            missile_state4 = "ready"
        if missile_state4 == "fire":
            fire_missile4(missile4X, missile4Y)
            missile4Y -= missile4Y_change

        if missile5Y <= 0:
            missile5Y = rocketshipY
            missile_state5 = "ready"
        if missile_state5 == "fire":
            fire_missile5(missile5X, missile5Y)
            missile5Y -= missile5Y_change

        level_count = 6
        if score_value == 250:
            level_up()
            player_life_count = 3
            rocket_shield = 150

        rockY += rockY_change
        rockX += rockX_change
        if rockY >= 0:
            rockY_change = 10
            rockX_change = -2.5
        if rockY >= 2000:
            rockX = random.randint(200, 715)
            rockY = random.randint(0, 0)
        rock(rockX, rockY)
        for i in range(num_of_terrors):

            collisionimpact2 = terrorimpact1(terrorX[i], terrorY[i], missile2X, missile2Y)
            if collisionimpact2 and missile_state2 == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missile2Y = rocketshipY
                missile_state2 = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

            collisionimpact4 = terrorimpact4(terrorX[i], terrorY[i], missile4X, missile4Y)
            if collisionimpact4 and missile_state4 == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missile4Y = rocketshipY
                missile_state4 = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

            collisionimpact5 = terrorimpact5(terrorX[i], terrorY[i], missile5X, missile5Y)
            if collisionimpact5 and missile_state5 == "fire":
                screen.blit(explosionimg, (terrorX[i], terrorY[i]))
                explosion = mixer.Sound('photos/explosion.wav')
                explosion.play()
                missile5Y = rocketshipY
                missile_state5 = "ready"
                score_value += 1
                terrorX[i] = random.randint(0, 736)
                terrorY[i] = random.randint(-150, -10)

        rockcollision1 = rockCollision(rockX, rockY, rocketshipX, rocketshipY)
        if rockcollision1:
            rocket_shield -= 75
            screen.blit(explosionimg, (rocketshipX, rocketshipY))
            boom1 = mixer.Sound('photos/earthquake.wav')
            boom1.play()
            rockX = random.randint(200, 715)
            rockY = random.randint(0, 0)
            if rocket_shield <= 0:
                player_life_count += -1
                rockX = random.randint(200, 715)
                rockY = random.randint(0, 0)
                if player_life_count == 2:
                    rocket_shield = 150
                    rockX = random.randint(200, 715)
                    rockY = random.randint(0, 0)
                if player_life_count == 1:
                    rocket_shield = 150
                    rockX = random.randint(200, 715)
                    rockY = random.randint(0, 0)
        rock(rockX, rockY)
    if score_value == 349:
        rocket_shield = 150
        player_life_count = 3

    if score_value == 350:
        rock(rockX, rockY)
        boss1_shield_bar(screen, boss1_shield)
        level_count = "boss level"
        for i in range(num_of_terrors):
            terrorY[i] = -5000
        boss1(boss1X, boss1Y)
        boss1X += boss1X_change
        boss1Y += boss1Y_change
        if boss1Y <= 0:
            boss1Y_change = 4.5
        if boss1Y >= 470:
            boss1Y_change = -4.5
        if boss1X <= 0:
            boss1X_change = 2
        if boss1X >= 650:
            boss1X_change = -2

        if missile6Y <= 0:
            missile6Y = rocketshipY
            missile_state6 = "ready"
        if missile_state6 == "fire":
            fire_missile6(missile6X, missile6Y)
            missile6Y -= missile6Y_change

        if missile7Y <= 0:
            missile7Y = rocketshipY
            missile_state7 = "ready"
        if missile_state7 == "fire":
            fire_missile7(missile7X, missile7Y)
            missile7Y -= missile7Y_change

        if missile8Y <= 0:
            missile8Y = rocketshipY
            missile_state8 = "ready"
        if missile_state8 == "fire":
            fire_missile8(missile8X, missile8Y)
            missile8Y -= missile8Y_change

        bossimpact = boss1impact(boss1X, boss1Y, missileX, missileY)
        if bossimpact and missile_state == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missileY = rocketshipY
            missile_state = "ready"

        bossimpact1 = boss1impact1(boss1X, boss1Y, missile1X, missile1Y)
        if bossimpact1 and missile_state1 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile1Y = rocketshipY
            missile_state1 = "ready"

        bossimpact2 = boss1impact2(boss1X, boss1Y, missile2X, missile2Y)
        if bossimpact2 and missile_state2 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile2Y = rocketshipY
            missile_state2 = "ready"

        bossimpact3 = boss1impact3(boss1X, boss1Y, missile3X, missile3Y)
        if bossimpact3 and missile_state3 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile3Y = rocketshipY
            missile_state3 = "ready"

        bossimpact4 = boss1impact4(boss1X, boss1Y, missile4X, missile4Y)
        if bossimpact4 and missile_state4 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile4Y = rocketshipY
            missile_state4 = "ready"

        bossimpact5 = boss1impact5(boss1X, boss1Y, missile5X, missile5Y)
        if bossimpact5 and missile_state5 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile5Y = rocketshipY
            missile_state5 = "ready"

        bossimpact6 = boss1impact6(boss1X, boss1Y, missile6X, missile6Y)
        if bossimpact6 and missile_state6 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile6Y = rocketshipY
            missile_state6 = "ready"

        bossimpact7 = boss1impact7(boss1X, boss1Y, missile7X, missile7Y)
        if bossimpact7 and missile_state7 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile7Y = rocketshipY
            missile_state7 = "ready"

        bossimpact8 = boss1impact8(boss1X, boss1Y, missile8X, missile8Y)
        if bossimpact8 and missile_state8 == "fire":
            boss1_shield -= 20
            screen.blit(explosionimg, (boss1X, boss1Y))
            explosion20 = mixer.Sound('photos/explosion.wav')
            explosion20.play()
            missile8Y = rocketshipY
            missile_state8 = "ready"

        rocketbossimpact = rocketboss(boss1X, boss1Y, rocketshipX, rocketshipY)
        if rocketbossimpact:
            player_life_count = 0
            player_shield = 0
            boom2 = mixer.Sound('photos/earthquake.wav')
            boom2.play()

        rock1Y += rock1Y_change
        rock1X += rock1X_change
        if rock1Y >= 0:
            rock1Y_change = 10
            rock1X_change = 2.5
        if rock1Y >= 1800:
            rock1X = random.randint(0, 500)
            rock1Y = random.randint(0, 0)
        rock1(rock1X, rock1Y)

        if boss1_shield <= 0:
            boss1Y_change = 0
            boss1X_change = 0
            victory_text()
            forward()

        rockcollision2 = rock1Collision(rock1X, rock1Y, rocketshipX, rocketshipY)
        if rockcollision2:
            rocket_shield -= 100
            screen.blit(explosionimg, (rocketshipX, rocketshipY))
            boom1 = mixer.Sound('photos/earthquake.wav')
            boom1.play()
            rock1X = random.randint(0, 500)
            rock1Y = random.randint(0, 0)
            if rocket_shield <= 0:
                player_life_count += -1
                rock1X = random.randint(0, 500)
                rock1Y = random.randint(0, 0)
                if player_life_count == 2:
                    rocket_shield = 150
                    rock1X = random.randint(0, 500)
                    rock1Y = random.randint(0, 0)
                if player_life_count == 1:
                    rocket_shield = 150
                    rock1X = random.randint(0, 500)
                    rock1Y = random.randint(0, 0)
        rock1(rock1X, rock1Y)
    if score_value >= 351:
        rock1Y += rock1Y_change
        rock1X += rock1X_change
        if rock1Y >= 0:
            rock1Y_change = 10
            rock1X_change = 2.5
        if rock1Y >= 1800:
            rock1X = random.randint(0, 500)
            rock1Y = random.randint(0, 0)
        rock1(rock1X, rock1Y)
        rockcollision2 = rock1Collision(rock1X, rock1Y, rocketshipX, rocketshipY)
        if rockcollision2:
            rocket_shield -= 100
            screen.blit(explosionimg, (rocketshipX, rocketshipY))
            boom1 = mixer.Sound('photos/earthquake.wav')
            boom1.play()
            rock1X = random.randint(0, 500)
            rock1Y = random.randint(0, 0)
            if rocket_shield <= 0:
                player_life_count += -1
                rock1X = random.randint(0, 500)
                rock1Y = random.randint(0, 0)
                if player_life_count == 2:
                    rocket_shield = 150
                    rock1X = random.randint(0, 500)
                    rock1Y = random.randint(0, 0)
                if player_life_count == 1:
                    rocket_shield = 150
                    rock1X = random.randint(0, 500)
                    rock1Y = random.randint(0, 0)
        level_count = "infinit"

    next_level(level_countX, level_countY)
    show_score(textX, textY)
    show_life(lifeX, lifeY)
    pygame.display.update()
