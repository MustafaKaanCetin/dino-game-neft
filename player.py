import pygame
import random

from pygame.time import Clock

import config
import time

class Player:
    def __init__(self):
        self.x, self.y = 50, 80
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.jump = False
        self.duck_down = False
        self.alive = True

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)

    def env_collision(self, env):
        for e in config.elements:
            return pygame.Rect.colliderect(self.rect, e.ptero_rect) or \
            pygame.Rect.colliderect(self.rect, e.cacti_rect)

    def update(self, ground):
        if not (self.ground_collision(ground) or self.env_collision(config.elements)):
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
        else:
            self.alive = False
            self.jump = False
            self.vel = 0

    def jump_up(self):
        if not self.jump:
            self.jump = True
            self.vel = -5
        if self.vel >= 3:
            self.jump = False

    def duck(self):
        if not self.duck_down:
            self.duck_down = True
        #Didn't think how to quit the ducking sequence.

