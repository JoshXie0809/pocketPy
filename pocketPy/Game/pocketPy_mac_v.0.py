import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((480, 360))

# iconImg = pygame.image.load("icon.png")
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()
