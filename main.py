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
PLAYER_VELO = 5
window = pygame.display.set_mode((WIDTH, HEIGHT))


class Character(pygame.sprite.Sprite):
    COLOR = (255, 255, 255)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velo = 0
        self.y_velo = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    
    def movement(self, displacement_x, displacement_y):
        self.rect.x += displacement_x
        self.rect.y += displacement_y

    def move_left(self, velo):
        self.x_velo = -velo
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, velo):
        self.x_velo = velo
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.movement(self.x_velo, self.y_velo)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


def create_background(name):
    img = pygame.image.load(join("assets", "background", name))
    _, _, width, height = img.get_rect()
    tiles = []

    for x_tile in range(WIDTH // width + 1):
        for y_tile in range(HEIGHT // height + 1):
            position = (x_tile * width, y_tile * height)
            tiles.append(position)

    return tiles, img


def draw_img(window, background, background_img, char):
    for tile in background:
        window.blit(background_img, tile)

    char.draw(window)

    pygame.display.update()


def movement_handler(char):
    keys = pygame.key.get_pressed()

    char.x_velo = 0
    if keys[pygame.K_LEFT]:
        char.move_left(PLAYER_VELO)
    if keys[pygame.K_RIGHT]:
        char.move_right(PLAYER_VELO)


def main(window):
    clock = pygame.time.Clock()
    background, background_img = create_background("Purple.png")
    char = Character(100, 100, 30, 30)

    is_running = True
    while is_running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break

        char.loop(FPS)
        movement_handler(char)
        draw_img(window, background, background_img, char)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
