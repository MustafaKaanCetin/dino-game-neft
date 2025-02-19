import pygame
import sys
import random
import conf
import env
import dino

pygame.init()
pygame.display.set_caption("Dino Game NN")
dino = dino.Dino()
clock = pygame.time.Clock()

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def set_obj():
    new_obj = random.choice([env.SmallCactus(), env.LargeCactus(), env.CactusGroup(), env.Ptero()])
    if isinstance(new_obj, env.CactusGroup):
        for cactus in new_obj.cacti:
            conf.obj.append(cactus)
    else:
        conf.obj.append(new_obj)

def main():
    obj_spawn_time = 42
    speed = 5
    while True:
        quit_game()
        conf.window.fill((255, 255, 255))
        dino.update()
        dino.draw()
        conf.ground.draw()

        if obj_spawn_time == 0:
            set_obj()
            obj_spawn_time = random.randint(100, 200)

        for obj in conf.obj:
            obj.rect.x -= speed
            obj.draw(conf.window)
            if obj.rect.x < -obj.width:
                obj.out = True

        for obj in conf.obj:
            if obj.out:
                conf.obj.remove(obj)

        clock.tick(60)
        obj_spawn_time -= 1
        speed += 0.0001
        if not dino.alive:
            conf.obj = []
            speed = 5
            dino.alive = True
        pygame.display.flip()

main()



