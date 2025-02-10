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
    x = 5
