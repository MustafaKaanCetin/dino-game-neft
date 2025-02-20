import pygame
import random
from neural import Brain

import conf

class Dino:
    def __init__(self):
        self.x = 50
        self.y = conf.ground.ground_level - 40
        self.height = 15
        self.width = 10
        self.vel = 0
        self.duck_rect = pygame.Rect(self.x, conf.ground.ground_level - self.width, self.height, self.width)
        self.stand_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.curr_rect = self.stand_rect
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.alive = True
        self.jumping = False

        self.survival_time = 0
        self.decision = None
        self.fitness = 0
        self.input_size = 3
        self.brain = Brain(self.input_size)
        self.brain.generate_net()

    def update(self):
        self.y += self.vel
        self.curr_rect.y = self.y
        if not(self.obj_collision() or self.ground_collision(conf.ground)):
            self.vel += 0.25
        elif not(self.obj_collision()) and self.ground_collision(conf.ground):
            self.vel = 0
            if self.curr_rect.height == 15:
                self.y = conf.ground.ground_level - 15
            else:
                self.y = conf.ground.ground_level - 10
            self.curr_rect.y = self.y
            self.jumping = False
        else:
            self.alive = False

    def jump(self):
        if not self.jumping:
            self.curr_rect = self.stand_rect
            self.y = self.curr_rect.y
            self.height = self.curr_rect.height
            self.vel = -5.5
            self.jumping = True

    def duck(self):
        if not self.jumping:
            self.curr_rect = self.duck_rect
            self.y = self.curr_rect.y
            self.height = self.curr_rect.height
            self.width = self.curr_rect.width


    def draw(self):
        pygame.draw.rect(conf.window, self.color, self.curr_rect)

    def obj_collision(self):
        for obj in conf.obj:
            if pygame.Rect.colliderect(self.curr_rect, obj.rect):
                return True
        return False

    def ground_collision(self, ground):
        return self.y + self.height >= ground.ground_level

    @staticmethod
    def check_next_obj():
        for obj in conf.obj:
            if not obj.out:
                return obj
        return None

    def inputs(self):
        obj = self.check_next_obj()
        if obj:
            obj_height = obj.rect.height
            obj_dist = obj.rect.x - self.x
            return [(obj_height / 60) * 2 - 1, (obj_dist / conf.win_width) * 2 - 1, (self.vel / 5) * 2 - 1, (obj.above_ground / 10) * 2 - 1]
        return [0.05, 1.05, 0.05, -1]

    def think(self):
        output = self.brain.feed_forward(self)
        if output[0] > output[1]:
            self.jump()
        else:
            self.duck()
        self.decision = output

    def calculate_fitness(self):
        self.fitness = self.survival_time ** 2

    def copy(self):
        copy = Dino()
        copy.fitness = self.fitness
        copy.brain = self.brain.copy()
        copy.brain.generate_net()
        return copy