import pygame
import sys

path = '/Users/xiezhengqi/Desktop/GitHub/pocketPy/pocketPy/Game'

pygame.init()
screenSize = (480, 360)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('pocketPy mac v 0.0')
iconImg = pygame.image.load(path + "/icon.png")
pygame.display.set_icon(iconImg)


running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()
