import random

import pygame
import conf

class Ground:
    ground_level = 200
    def __init__(self, window):
        self.window = window
        self.x = 0
        self.y = self.ground_level
        self.rect = pygame.Rect(0, self.ground_level, conf.win_width, conf.win_height - self.ground_level)

    def draw(self):
        pygame.draw.rect(self.window, (0, 0, 0), self.rect)

class Obj:
    out = False
    color = (0, 0, 0)
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):

        pygame.draw.rect(window, self.color, self.rect)

class Cacti(Obj):
    def __init__(self, width, height):
        super().__init__(conf.win_width, conf.ground.ground_level - self.height, width, height, (0, 0, 0))

class SmallCactus(Cacti):
    width = 10
    height = 20
    def __init__(self):
        super().__init__(self.width, self.height)

class LargeCactus(Cacti):
    width = 10
    height = 40
    def __init__(self):
        super().__init__(self.width, self.height)

class CactusGroup:
    def __init__(self):
        self.cacti = []
        self.cactus_amount = random.choice([2, 3])
        for i in range(self.cactus_amount):
            cactus = random.choice([SmallCactus(), LargeCactus()])
            cactus.x = conf.win_width + i * 10 + 15
            cactus.rect = pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)
            self.cacti.append(cactus)

    def add(self, cactus):
        self.cacti.append(cactus)

class Ptero(Obj):
    width = 20
    height = 60
    def __init__(self):
        super().__init__(conf.win_width, conf.ground.ground_level - self.height - 10, self.width, self.height, (0, 0, 0))