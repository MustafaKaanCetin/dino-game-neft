import pygame
import random

import conf

class Dino:
    def __init__(self):
        self.x = 50
        self.y = conf.ground.ground_level - 40
        self.height = 15
        self.width = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 0
        self.alive = True
        self.jumping = False
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def update(self):
        self.y += self.vel
        if not(self.obj_collision() or self.ground_collision(conf.ground)):
            self.vel += 0.25
        elif not(self.obj_collision()) and self.ground_collision(conf.ground):
            self.vel = 0
            self.y = conf.ground.ground_level - 40
            self.jumping = False
        else:
            self.alive = False

    def jump(self):
        if not self.jumping:
            self.vel = -7.5
            self.jumping = True

    def duck(self):
        pass

    def draw(self):
        pygame.draw.rect(conf.window, self.color, (self.x, self.y, self.width, self.height))

    def obj_collision(self):
        for obj in conf.obj:
            if pygame.Rect.colliderect(self.rect, obj.rect):
                return True
        return False

    def ground_collision(self, ground):
        return self.y + self.height >= ground.ground_level