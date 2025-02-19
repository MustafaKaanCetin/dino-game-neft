import pygame
import env

win_width = 1200
win_height = 300
window = pygame.display.set_mode((win_width, win_height))

ground = env.Ground(window)
obj = []