import pygame
import random

from pygame.time import Clock

import config
import time

from config import ground


class Player:
    def __init__(self):
        self.x, self.y = 10, 70
        self.rect = pygame.Rect(self.x, self.y, 10, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.jump = False
        self.duck_down = False
        self.alive = True

    def draw(self):
        pygame.draw.rect(config.window, self.color, self.rect)

    def ground_collision(self):
        return pygame.Rect.colliderect(self.rect, config.ground)

    def env_collision(self):
        for e in config.elements:
            return pygame.Rect.colliderect(self.rect, e.rect) or \
            pygame.Rect.colliderect(self.rect, e.rect)

    def update(self):
        if not (self.ground_collision() or self.env_collision()):
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
        elif self.env_collision():
            self.alive = False
        else:
            self.jump = False
            self.vel = 0
            self.y = 20

    def jump_up(self):
        if not self.jump:
            self.jump = True
            self.vel = -5
        if self.ground_collision():
            self.jump = False

    def duck(self):
        if not self.duck_down:
            self.duck_down = True
            self.rect = pygame.Rect(self.x, self.y+10, 20, 10)

    def unduck(self):
        if self.duck_down:
            self.duck_down = False
            self.rect = pygame.Rect(self.x, self.y, 10, 20)

    @staticmethod
    def closest_obstacle():
        for e in config.elements:
            if not e.passed:
                return e


