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

class Bird:
    x = 5

class Cactus:
    def __init__(self, win_width, width, height):
        self.x = win_width
        self.width = width
        self.height = height
        self.off_screen = False

    def update(self):
        self.x -= 1
        if self.x <= -self.width:
            self.off_screen = True

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.x, Ground.ground_level - self.height, self.width, self.height))

# Sizes of cacti will change in the future
class SmallCactus(Cactus):
    def __init__(self, win_width, width, height):
        super().__init__(win_width, 5, 10)

class LargeCactus(Cactus):
    def __init__(self, win_width, width, height):
        super().__init__(win_width, 10, 15)

class MultiCactus(Cactus):
    def __init__(self, win_width, width, height):
        super().__init__(win_width, 20, 15)

class Cloud:
    x = 5
    y = 5
