import pygame
from .tower import Tower
import os
import math
import time

range_imgs = [pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "support_tower_1_000.png")).convert_alpha(), (90, 90)),
    pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/tower_sprites", "support_tower_1_000.png")).convert_alpha(),
        (90, 90))]

plusimg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "plus1.png")).convert_alpha(),
                                 (14, 14))


class RangeTower(Tower):
    """
    Add extra range to each surrounding tower
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.effect = [0.2, 0.4]
        self.effected = []
        self.effected1 = []
        self.tower_imgs = range_imgs[:]
        self.width = self.height = 90
        self.name = "range"
        self.lives = 10
        self.price = [750]
        self.sell_price = [750]

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def support(self, towers):
        """
        will modify towers according to abillity
        :param towers: list
        :return: None
        """

        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                self.effected.append(tower)

        for tower in self.effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level - 1])
            if dis >= self.range + tower.width / 2:
                self.effected.remove(tower)


damage_imgs = [pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/tower_sprites", "support_tower_000.png")).convert_alpha(), (90, 90)),
    pygame.transform.scale(pygame.image.load(
        os.path.join("game_assets/tower_sprites", "support_tower_000.png")).convert_alpha(), (90, 90))]


class DamageTower(RangeTower):
    """
    add damage to surrounding towers
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_imgs = damage_imgs[:]
        self.effect = [0.5, 1]
        self.name = "damage"
        self.price = [750]
        self.sell_price = [750]

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                self.effected1.append(tower)

        for tower in self.effected1:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level - 1])
            if dis >= self.range + tower.width / 2:
                self.effected1.remove(tower)
