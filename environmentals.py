import pygame
import random

class Ground:
    ground_level = 100

    def __init__(self, win_width):
        self.x = 0
        self.y = Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 3)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)

class Pterodactyl:
    speed = 1
    width = 10
    height = 5
    def __init__(self, win_width):
        self.x = win_width
        self.speed = Pterodactyl.speed
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.off_screen = False
        self.passed = False

    def update(self):
        self.x -= self.speed
        if self.x <= -self.width:
            self.off_screen = True
        if self.x + Pterodactyl.width <= 50:
            self.passed = True

    def draw(self, window):
        self.rect = pygame.Rect(self.x, Ground.ground_level - Pterodactyl.height - 20, Pterodactyl.width, Pterodactyl.height)
        pygame.draw.rect(window, (255, 255, 255), self.rect)

class Cactus:
    speed = 1
    def __init__(self, win_width, width, height):
        self.x = win_width
        self.width = width
        self.height = height
        self.speed = Cactus.speed
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.off_screen = False
        self.passed = False

    def update(self):
        self.x -= self.speed
        if self.x <= -self.width:
            self.off_screen = True
        if self.x + self.width <= 50:
            self.passed = True

    def draw(self, window):
        self.rect = pygame.Rect(self.x, Ground.ground_level - self.height, self.width, self.height)
        pygame.draw.rect(window, (255, 255, 255), self.rect)

# Sizes of cacti will change in the future
class SmallCactus(Cactus):
    def __init__(self, win_width):
        super().__init__(win_width, 5, 10)

class LargeCactus(Cactus):
    def __init__(self, win_width):
        super().__init__(win_width, 5, 15)

class MultiCactus(Cactus):
    def __init__(self, win_width):
        super().__init__(win_width, 15, 10)

class Cloud:
    def __init__(self, win_width):
        self.x = win_width
        self.width = 20
        self.height = 10
        self.cloud_rect = pygame.Rect(0,0,0,0)
        self.off_screen = False
