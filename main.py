import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


SIZE = WIDTH, HEIGHT = 700, 400
pygame.init()
screen = pygame.display.set_mode(SIZE)
screen.fill('black')
is_draw = False
running = True
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("arrow.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            sprite.rect.x = x
            sprite.rect.y = y
            screen.fill('black')
            all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
