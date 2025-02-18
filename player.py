import pygame
import random
import brain_struct

from pygame.time import Clock

import config
import time

from config import ground


class Player:
    def __init__(self):
        self.x, self.y = 10, 60
        self.rect = pygame.Rect(self.x, self.y, 10, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.jump = False
        self.duck_down = False
        self.alive = True

        self.lifespan = 0
        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.fitness = 0
        self.inputs = 3
        self.brain = brain_struct.Brain(self.inputs)
        self.brain.generate_net()

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
            self.lifespan += 1
        elif self.env_collision():
            self.alive = False
        elif self.ground_collision():
            self.vel = -5

    def jump_up(self):
        if self.ground_collision():
            self.vel = -5
            self.jump = True
            print("Jumped")

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

    def look(self):
        if config.elements:
            self.vision[0] = max(0, self.rect.center[1]-self.closest_obstacle().rect.bottom) / 500
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.elements[0].rect.bottom))
            self.vision[1] = max(0, self.closest_obstacle().x - self.rect.center[0]) / 500
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (config.elements[0].x, self.rect.center[1]))
            self.vision[2] = max(0, self.closest_obstacle().rect.top - self.rect.center[1]) / 500
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.elements[0].rect.top))

    def think(self):
        self.decision = self.brain.feed_forward(self.vision)
        if self.decision >= 0.7:
            self.jump_up()

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player()
        clone.fitness = self.fitness
        clone.brain = self.brain.clone()
        clone.brain.generate_net()
        return clone



