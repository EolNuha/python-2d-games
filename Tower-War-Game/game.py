import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from enemies.sword import Sword
from enemies.goblin import Goblin
from towers.archerTower import ArcherTowerLong, ArcherTowerShort, ArcherTowerMedium, ArcherTowerStrong
from towers.supportTower import DamageTower, RangeTower
from menu.menu import VerticalMenu, PlayPauseButton, HorizontalMenu
import time
import random
import math

pygame.font.init()
pygame.init()

pygame.display.set_caption("Tower War")
icon = pygame.image.load(os.path.join("game_assets", "icon.png"))
pygame.display.set_icon(icon)
VictoryImg = pygame.image.load(os.path.join("game_assets", "victory.png"))
DefeatImg = pygame.image.load(os.path.join("game_assets", "defeat.png"))
stars_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")).convert_alpha(),
                                   (80, 80))
start_btn = pygame.image.load(os.path.join("game_assets", "menu_button.png")).convert_alpha()

path = [(-10, 240), (19, 240), (65, 240), (140, 230), (231, 249), (155, 220), (165, 220), (177, 210), (185, 220),
        (467, 280), (282, 270), (345, 275), (380, 270),
        (526, 277), (650, 235), (624, 268), (715, 105),
        (715, 205), (700, 150), (796, 50), (870, 25), (923, 127), (930, 222), (990, 224), (1065, 270), (1105, 305),
        (1180, 366),
        (1150, 458), (1080, 505), (1013, 500),
        (916, 500), (894, 510), (800, 550), (718, 560), (645, 560), (580, 560), (530, 550), (476, 560), (428, 556),
        (363, 555), (295, 555), (249, 555), (200, 555), (148, 541),
        (10, 442), (99, 455), (99, 475), (84, 393), (26, 358), (-20, 335), (-75, 305), (-100, 345)]

lives_img = pygame.image.load(os.path.join("game_assets", "heart.png")).convert_alpha()
star_img = pygame.image.load(os.path.join("game_assets", "star.png")).convert_alpha()
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu2.png")).convert_alpha(),
                                  (120, 535))
down_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "wave3.png")).convert_alpha(),
                                  (230, 150))

buy_archer = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "tower_sprite_000.png")).convert_alpha(),
    (75, 75))
buy_archer_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "tower_sprite_2_000.png")).convert_alpha(), (75, 75))
buy_archer_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "tower_sprite_3_000.png")).convert_alpha(), (75, 75))
buy_archer_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "tower_sprite_4_000.png")).convert_alpha(), (75, 75))
buy_damage = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "support_tower_000.png")).convert_alpha(),
    (60, 60))
buy_range = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "support_tower_1_000.png")).convert_alpha(),
    (60, 60))

play_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "button_play.png")).convert_alpha(),
                                  (75, 75))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "button_pause.png")).convert_alpha(),
                                   (75, 75))

sound_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "button_sound.png")).convert_alpha(),
                                   (75, 75))
sound_btn_off = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets", "button_sound_off.png")).convert_alpha(), (75, 75))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "wave1.png")).convert_alpha(), (225, 75))

attack_tower_names = ["archer", "archer2", "archer3", "archer4"]
support_tower_names = ["range", "damage"]

# load music
pygame.mixer.music.load(os.path.join("game_assets", "music.wav"))

# waves are in form
# frequency of enemies
# (# scorpions, # wizards, # clubs, # goblin, # swords)
waves = [
    [20, 0, 0, 0],
    [40, 5, 0, 0],
    [80, 10, 0, 0],
    [100, 25, 0, 0],
    [80, 30, 0, 0, 0],
    [70, 45, 0, 0],
    [70, 50, 0, 0],
    [70, 55, 0, 0],
    [70, 60, 0, 0],
    [70, 65, 0, 0, 1],
    [20, 65, 10, 0],
    [20, 65, 15, 0],
    [10, 70, 35, 0],
    [0, 70, 40, 0],
    [0, 20, 75, 0, 3],
    [0, 100, 50, 10],
    [0, 40, 60, 10],
    [0, 100, 50, 15],
    [0, 80, 80, 20],
    [0, 80, 100, 45, 4],
    [0, 0, 0, 0]

]

clock = pygame.time.Clock()


class Game:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.win = win
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
        self.lives = 10
        self.money = 2000
        self.FPS = 1000
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = []
        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 286, side_img)
        self.menu.add_btn(buy_archer, "buy_archer", 500)
        self.menu.add_btn(buy_archer_2, "buy_archer_2", 750)
        self.menu.add_btn(buy_archer_4, "buy_archer_4", 1000)
        self.menu.add_btn(buy_archer_3, "buy_archer_3", 1500)
        self.menu1 = HorizontalMenu(self.width - down_img.get_width() - side_img.get_width() + 125, 670, down_img)
        self.menu1.add_btn(buy_damage, "buy_damage", 1000)
        self.menu1.add_btn(buy_range, "buy_range", 1000)
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.music_on = True
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 85)
        self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, 90, self.height - 85)
        self.btn = (self.width / 2 - start_btn.get_width() / 2, 450, start_btn.get_width(), start_btn.get_height())

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0 and self.wave <= 19 and not self.lives == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = self.pause
        else:
            wave_enemies = [Scorpion(), Wizard(), Club(), Goblin(), Sword()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        pygame.mixer.music.play(loops=-1)
        run = True
        while run:
            if self.wave >= 20:
                self.wave = 998
            if not self.pause:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1, 6) / 3:
                    self.timer = time.time()
                    self.gen_enemies()

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)
                if not self.point_to_line(self.moving_object):
                    self.moving_object.place_color = (255, 0, 0, 100)
                else:
                    self.moving_object.place_color = (0, 0, 255, 100)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.wave = 0

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            run = False
                    # if you're moving an object and click
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        # check for play or pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not self.pause
                            self.playPauseButton.paused = self.pause

                        if self.soundButton.click(pos[0], pos[1]):
                            self.music_on = not self.music_on
                            self.soundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # look if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                        down_menu_button = self.menu1.get_clicked(pos[0], pos[1])
                        if down_menu_button:
                            cost = self.menu1.get_item_cost(down_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_support_tower(down_menu_button)

                        # look if you clicked on attack tower or support tower
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked == "Upgrade":
                                cost = self.selected_tower.sell()
                                self.money += cost
                                self.selected_tower.sold()
                                btn_clicked = None

                        if not btn_clicked:

                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # look if you clicked on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

            # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.enemys:
                    en.move()
                    if en.x < -15:
                        to_del.append(en)

                # delete all enemies off the screen
                for d in to_del:
                    self.lives -= 1
                    self.enemys.remove(d)

                # loop through attack towers
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemys)

                # loop through attack towers
                for tw in self.support_towers:
                    tw.support(self.attack_towers)

                # if you lose
                if self.lives <= 0:
                    self.wave = 0
                    self.enemys = []

            clock.tick(self.FPS)
            self.draw()

    def point_to_line(self, tower):
        """
        returns if you can place tower based on distance from
        path
        :param tower: Tower
        :return: Bool
        """
        x, y = path[0]
        x1, y1 = path[1]
        x2, y2 = path[2]
        x3, y3 = path[3]
        x4, y4 = path[4]
        x5, y5 = path[5]
        x6, y6 = path[6]
        x7, y7 = path[7]
        x8, y8 = path[8]
        x9, y9 = path[9]
        x10, y10 = path[10]
        x11, y11 = path[11]
        x12, y12 = path[12]
        x13, y13 = path[13]
        x14, y14 = path[14]
        x15, y15 = path[15]
        x16, y16 = path[16]
        x17, y17 = path[17]
        x18, y18 = path[18]
        x19, y19 = path[19]
        x20, y20 = path[20]
        x21, y21 = path[21]
        x22, y22 = path[22]
        x23, y23 = path[23]
        x24, y24 = path[24]
        x25, y25 = path[25]
        x26, y26 = path[26]
        x27, y27 = path[27]
        x28, y28 = path[28]
        x29, y29 = path[29]
        x30, y30 = path[30]
        x31, y31 = path[31]
        x32, y32 = path[32]
        x33, y33 = path[33]
        x34, y34 = path[34]
        x35, y35 = path[35]
        x36, y36 = path[36]
        x37, y37 = path[37]
        x38, y38 = path[38]
        x39, y39 = path[39]
        x40, y40 = path[40]
        x41, y41 = path[41]
        x42, y42 = path[42]
        x43, y43 = path[43]
        x44, y44 = path[44]
        x45, y45 = path[45]
        x46, y46 = path[46]
        x47, y47 = path[47]
        x48, y48 = path[48]
        x49, y49 = path[49]
        x50, y50 = path[50]
        x51, y51 = path[51]

        dis = math.sqrt((x - self.moving_object.x) ** 2 + (y - self.moving_object.y - 25) ** 2)
        dis1 = math.sqrt((x1 - self.moving_object.x) ** 2 + (y1 - self.moving_object.y - 25) ** 2)
        dis2 = math.sqrt((x2 - self.moving_object.x) ** 2 + (y2 - self.moving_object.y - 25) ** 2)
        dis3 = math.sqrt((x3 - self.moving_object.x) ** 2 + (y3 - self.moving_object.y - 35) ** 2)
        dis4 = math.sqrt((x4 - self.moving_object.x) ** 2 + (y4 - self.moving_object.y - 35) ** 2)
        dis5 = math.sqrt((x5 - self.moving_object.x) ** 2 + (y5 - self.moving_object.y - 25) ** 2)
        dis6 = math.sqrt((x6 - self.moving_object.x) ** 2 + (y6 - self.moving_object.y) ** 2)
        dis7 = math.sqrt((x7 - self.moving_object.x) ** 2 + (y7 - self.moving_object.y) ** 2)
        dis8 = math.sqrt((x8 - self.moving_object.x) ** 2 + (y8 - self.moving_object.y) ** 2)
        dis9 = math.sqrt((x9 - self.moving_object.x) ** 2 + (y9 - self.moving_object.y) ** 2)
        dis10 = math.sqrt((x10 - self.moving_object.x) ** 2 + (y10 - self.moving_object.y) ** 2)
        dis11 = math.sqrt((x11 - self.moving_object.x) ** 2 + (y11 - self.moving_object.y) ** 2)
        dis12 = math.sqrt((x12 - self.moving_object.x) ** 2 + (y12 - self.moving_object.y) ** 2)
        dis13 = math.sqrt((x13 - self.moving_object.x) ** 2 + (y13 - self.moving_object.y) ** 2)
        dis14 = math.sqrt((x14 - self.moving_object.x) ** 2 + (y14 - self.moving_object.y) ** 2)
        dis15 = math.sqrt((x15 - self.moving_object.x) ** 2 + (y15 - self.moving_object.y) ** 2)
        dis16 = math.sqrt((x16 - self.moving_object.x) ** 2 + (y16 - self.moving_object.y) ** 2)
        dis17 = math.sqrt((x17 - self.moving_object.x) ** 2 + (y17 - self.moving_object.y) ** 2)
        dis18 = math.sqrt((x18 - self.moving_object.x) ** 2 + (y18 - self.moving_object.y) ** 2)
        dis19 = math.sqrt((x19 - self.moving_object.x) ** 2 + (y19 - self.moving_object.y) ** 2)
        dis20 = math.sqrt((x20 - self.moving_object.x) ** 2 + (y20 - self.moving_object.y) ** 2)
        dis21 = math.sqrt((x21 - self.moving_object.x) ** 2 + (y21 - self.moving_object.y) ** 2)
        dis22 = math.sqrt((x22 - self.moving_object.x) ** 2 + (y22 - self.moving_object.y) ** 2)
        dis23 = math.sqrt((x23 - self.moving_object.x) ** 2 + (y23 - self.moving_object.y) ** 2)
        dis24 = math.sqrt((x24 - self.moving_object.x) ** 2 + (y24 - self.moving_object.y) ** 2)
        dis25 = math.sqrt((x25 - self.moving_object.x) ** 2 + (y25 - self.moving_object.y) ** 2)
        dis26 = math.sqrt((x26 - self.moving_object.x) ** 2 + (y26 - self.moving_object.y) ** 2)
        dis27 = math.sqrt((x27 - self.moving_object.x) ** 2 + (y27 - self.moving_object.y) ** 2)
        dis28 = math.sqrt((x28 - self.moving_object.x) ** 2 + (y28 - self.moving_object.y) ** 2)
        dis29 = math.sqrt((x29 - self.moving_object.x) ** 2 + (y29 - self.moving_object.y) ** 2)
        dis30 = math.sqrt((x30 - self.moving_object.x) ** 2 + (y30 - self.moving_object.y) ** 2)
        dis31 = math.sqrt((x31 - self.moving_object.x) ** 2 + (y31 - self.moving_object.y) ** 2)
        dis32 = math.sqrt((x32 - self.moving_object.x) ** 2 + (y32 - self.moving_object.y) ** 2)
        dis33 = math.sqrt((x33 - self.moving_object.x) ** 2 + (y33 - self.moving_object.y) ** 2)
        dis34 = math.sqrt((x34 - self.moving_object.x) ** 2 + (y34 - self.moving_object.y) ** 2)
        dis35 = math.sqrt((x35 - self.moving_object.x) ** 2 + (y35 - self.moving_object.y) ** 2)
        dis36 = math.sqrt((x36 - self.moving_object.x) ** 2 + (y36 - self.moving_object.y) ** 2)
        dis37 = math.sqrt((x37 - self.moving_object.x) ** 2 + (y37 - self.moving_object.y) ** 2)
        dis38 = math.sqrt((x38 - self.moving_object.x) ** 2 + (y38 - self.moving_object.y) ** 2)
        dis39 = math.sqrt((x39 - self.moving_object.x) ** 2 + (y39 - self.moving_object.y) ** 2)
        dis40 = math.sqrt((x40 - self.moving_object.x) ** 2 + (y40 - self.moving_object.y) ** 2)
        dis41 = math.sqrt((x41 - self.moving_object.x) ** 2 + (y41 - self.moving_object.y) ** 2)
        dis42 = math.sqrt((x42 - self.moving_object.x) ** 2 + (y42 - self.moving_object.y) ** 2)
        dis43 = math.sqrt((x43 - self.moving_object.x) ** 2 + (y43 - self.moving_object.y) ** 2)
        dis44 = math.sqrt((x44 - self.moving_object.x) ** 2 + (y44 - self.moving_object.y) ** 2)
        dis45 = math.sqrt((x45 - self.moving_object.x) ** 2 + (y45 - self.moving_object.y) ** 2)
        dis46 = math.sqrt((x46 - self.moving_object.x) ** 2 + (y46 - self.moving_object.y) ** 2)
        dis47 = math.sqrt((x47 - self.moving_object.x) ** 2 + (y47 - self.moving_object.y) ** 2)
        dis48 = math.sqrt((x48 - self.moving_object.x) ** 2 + (y48 - self.moving_object.y) ** 2)
        dis49 = math.sqrt((x49 - self.moving_object.x) ** 2 + (y49 - self.moving_object.y) ** 2)
        dis50 = math.sqrt((x50 - self.moving_object.x) ** 2 + (y50 - self.moving_object.y) ** 2)
        dis51 = math.sqrt((x51 - self.moving_object.x) ** 2 + (y51 - self.moving_object.y) ** 2)

        if dis <= 50:
            return False
        elif dis1 <= 50:
            return False
        elif dis2 <= 50:
            return False
        elif dis3 <= 20:
            return False
        elif dis4 <= 40:
            return False
        elif dis5 <= 50:
            return False
        elif dis6 <= 20:
            return False
        elif dis7 <= 50:
            return False
        elif dis8 <= 50:
            return False
        elif dis9 <= 50:
            return False
        elif dis10 <= 50:
            return False
        elif dis11 <= 50:
            return False
        elif dis12 <= 50:
            return False
        elif dis13 <= 50:
            return False
        elif dis14 <= 50:
            return False
        elif dis15 <= 50:
            return False
        elif dis16 <= 50:
            return False
        elif dis17 <= 50:
            return False
        elif dis18 <= 50:
            return False
        elif dis19 <= 50:
            return False
        elif dis20 <= 50:
            return False
        elif dis21 <= 50:
            return False
        elif dis22 <= 40:
            return False
        elif dis23 <= 50:
            return False
        elif dis24 <= 50:
            return False
        elif dis25 <= 50:
            return False
        elif dis26 <= 50:
            return False
        elif dis27 <= 50:
            return False
        elif dis28 <= 50:
            return False
        elif dis29 <= 50:
            return False
        elif dis30 <= 50:
            return False
        elif dis31 <= 50:
            return False
        elif dis32 <= 50:
            return False
        elif dis33 <= 50:
            return False
        elif dis34 <= 50:
            return False
        elif dis35 <= 50:
            return False
        elif dis36 <= 50:
            return False
        elif dis37 <= 50:
            return False
        elif dis38 <= 50:
            return False
        elif dis39 <= 50:
            return False
        elif dis40 <= 50:
            return False
        elif dis41 <= 50:
            return False
        elif dis42 <= 50:
            return False
        elif dis43 <= 50:
            return False
        elif dis44 <= 50:
            return False
        elif dis45 <= 50:
            return False
        elif dis46 <= 50:
            return False
        elif dis47 <= 50:
            return False
        elif dis48 <= 50:
            return False
        elif dis49 <= 50:
            return False
        elif dis50 <= 50:
            return False
        elif dis51 <= 50:
            return False
        return True

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        if self.lives <= 0:
            self.win.blit(DefeatImg, (self.width / 2 - DefeatImg.get_width() / 2, 250))
            self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        if self.wave == 998:
            self.win.blit(VictoryImg, (self.width / 2 - VictoryImg.get_width() / 2, 200))
            self.win.blit(start_btn, (self.btn[0], self.btn[1]))
            if self.lives >= 8:
                self.win.blit(stars_img, (self.width / 2 - VictoryImg.get_width() / 2 + 160, 350))
                self.win.blit(stars_img, (self.width / 2 - VictoryImg.get_width() / 2 + 245, 350))
                self.win.blit(stars_img, (self.width / 2 - VictoryImg.get_width() / 2 + 330, 350))
            elif self.lives >= 4:
                self.win.blit(stars_img, (self.width / 2 - VictoryImg.get_width() / 2 + 200, 350))
                self.win.blit(stars_img, (self.width / 2 - VictoryImg.get_width() / 2 + 285, 350))
            else:
                self.win.blit(stars_img, (self.width / 2 - stars_img.get_width() / 2, 350))

        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)

            for tower in self.support_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)
        self.menu1.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(star_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        # draw wave
        self.win.blit(wave_bg, (10, 10))
        text = self.life_font.render("Wave #" + str(self.wave + 1), 1, (255, 255, 255))
        self.win.blit(text, (10 + wave_bg.get_width() / 2 - text.get_width() / 2, 25))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer", "buy_archer_2", "buy_archer_4", "buy_archer_3"]
        object_list = [ArcherTowerLong(x, y), ArcherTowerShort(x, y), ArcherTowerMedium(x, y), ArcherTowerStrong(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

    def add_support_tower(self, name):
        x, y = pygame.mouse.get_pos()
        tower_list = ["buy_damage", "buy_range"]
        support_list = [DamageTower(x, y), RangeTower(x, y)]

        try:
            sup = support_list[tower_list.index(name)]
            self.moving_object = sup
            sup.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")
