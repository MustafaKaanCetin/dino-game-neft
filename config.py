import environmentals
import pygame

window_width = 600
window_height = 150
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

ground = environmentals.Ground(window_width)