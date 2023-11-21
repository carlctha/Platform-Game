import os
import random
import math
import pygame

from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

BACKGROUND = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()

    is_running = True
    while is_running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
