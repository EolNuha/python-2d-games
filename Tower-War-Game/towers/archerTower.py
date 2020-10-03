import pygame
from .tower import Tower
import os
import math
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "wave1.png")).convert_alpha(), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")).convert_alpha(),
                                     (50, 50))

tower_imgs1 = []
archer_imgs1 = []
# load archer tower images
for x in range(0, 14):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    tower_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/tower_sprites/tower_sprite_0" + add_str + ".png")).convert_alpha(),
        (90, 90)))

# load archer images
for x in range(0, 6):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    archer_imgs1.append(
        pygame.image.load(os.path.join("game_assets/tower_sprites/tower_stone_0" + add_str + ".png")).convert_alpha())


class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.tower_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.sell_price = [350]
        self.name = "archer"

        self.menu = Menu(self, self.x, self.y, menu_bg, [350, 1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def draw(self, win):
        """
        draw the arhcer tower and animated archer
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
            self.tower_count += 4
            if self.tower_count >= len(self.tower_imgs) * 10:
                self.tower_count = 0
        else:
            self.archer_count = 0
            self.tower_count = 0

        archer = self.archer_imgs[self.archer_count // 10]
        tower_archer = self.tower_imgs[self.tower_count // 10]
        win.blit(archer, ((self.x - 10), (self.y - archer.get_height())))
        win.blit(tower_archer, (self.x + (-26) * 1.6, self.y + (-25) * 1.8))

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt(
                (self.x - enemy.img.get_width() / 2 - x + 15) ** 2 + (self.y - enemy.img.get_height() / 2 - y + 42) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 50:
                if first_enemy.hit(self.damage):
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money


tower_imgs = []
archer_imgs = []
# load archer tower images
for x in range(0, 15):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("game_assets/tower_sprites/tower_sprite_2_0" + add_str + ".png")).convert_alpha(),
        (90, 90)))
# load archer images
for x in range(0, 6):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    archer_imgs.append(
        pygame.image.load(os.path.join("game_assets/tower_sprites/tower_stone_0" + add_str + ".png")).convert_alpha())


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 175
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage
        self.sell_price = [500]

        self.menu = Menu(self, self.x, self.y, menu_bg, [500, 1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer2"


tower_imgs2 = []
archer_imgs2 = []
# load archer tower images
for x in range(0, 14):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    tower_imgs2.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("game_assets/tower_sprites/tower_sprite_3_0" + add_str + ".png")).convert_alpha(),
        (90, 90)))
# load archer images
for x in range(0, 6):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    archer_imgs2.append(
        pygame.image.load(os.path.join("game_assets/tower_sprites/tower_stone_0" + add_str + ".png")).convert_alpha())


class ArcherTowerStrong(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs2[:]
        self.archer_imgs = archer_imgs2[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 5
        self.original_damage = self.damage
        self.sell_price = [1000]

        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, 1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer3"


tower_imgs3 = []
archer_imgs3 = []
# load archer tower images
for x in range(0, 14):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    tower_imgs3.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("game_assets/tower_sprites/tower_sprite_4_0" + add_str + ".png")).convert_alpha(),
        (90, 90)))
# load archer images
for x in range(0, 6):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    archer_imgs3.append(
        pygame.image.load(os.path.join("game_assets/tower_sprites/tower_stone_0" + add_str + ".png")).convert_alpha())


class ArcherTowerMedium(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs3[:]
        self.archer_imgs = archer_imgs3[:]
        self.archer_count = 0
        self.range = 190
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 4
        self.original_damage = self.damage
        self.sell_price = [750]

        self.menu = Menu(self, self.x, self.y, menu_bg, [750, 1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer4"
