import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((480, 360))
path = '/Users/xiezhengqi/Desktop/GitHub/pocketPy/pocketPy/Game'
iconImg = pygame.image.load(path + "/icon.png")
pygame.display.set_icon(iconImg)
pygame.display.set_caption('pocketPy mac v 0.0')


running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()
