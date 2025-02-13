from random import Random

import pygame
from sys import exit
import config
import environmentals
import random

import player

pygame.init()
clock = pygame.time.Clock()
player_object = player.Player()

def generate_environment():
    element_dict = {0: environmentals.SmallCactus, 1: environmentals.LargeCactus, 2: environmentals.Pterodactyl}
    element = random.choice(list(element_dict.keys()))
    config.elements.append(element_dict[element](config.window_size[0]))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    cacti_spawn_time = 42
    while True:
        player_object.draw()
        quit_game()
        config.window.fill((0, 0, 0))
        config.ground.draw(config.window)
        if cacti_spawn_time <= 0:
            generate_environment()
            cacti_spawn_time = Random().randint(100, 200)
        cacti_spawn_time -= 1
        environmentals.Cactus.speed += 0.0001
        environmentals.Pterodactyl.speed += 0.0001
        for c in config.elements:
            c.speed = environmentals.Cactus.speed
            c.draw(config.window)
            c.update()
            if c.off_screen:
                config.elements.remove(c)
        if player_object.alive:
            player_object.draw()
            player_object.update()
        clock.tick(60)
        pygame.display.flip()

main()