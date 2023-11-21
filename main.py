import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 600, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def create_background(name):
    img = pygame.image.load(join("assets", "background", name))
    _, _, width, height = img.get_rect()
    tiles = []

    for x_tile in range(WIDTH // width + 1):
        for y_tile in range(HEIGHT // height + 1):
            position = (x_tile * width, y_tile * height)
            tiles.append(position)

    return tiles, img

def draw_img(window, background, background_img):
    for tile in background:
        window.blit(background_img, tile)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, background_img = create_background("Purple.png")

    is_running = True
    while is_running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
        
        draw_img(window, background, background_img)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
