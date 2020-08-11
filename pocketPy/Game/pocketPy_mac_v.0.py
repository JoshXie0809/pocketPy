import pygame
import sys
import numpy as np

path = '/Users/xiezhengqi/Desktop/GitHub/pocketPy/pocketPy/Game'

pygame.init()
screenSize = (480, 360)
clock = pygame.time.Clock()
pygame.display.set_caption('pocketPy mac v 0.0')
screen = pygame.display.set_mode(screenSize)
screen.fill((0, 0, 0))
pygame.display.update()


def start(event):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Pressed Enter to Go", True, (255, 255, 255))
    screen.blit(text, ((screenSize[0] - text.get_width()) // 2, 5/3*(screenSize[1] - text.get_height()) // 2))
    pygame.display.update()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K



done = False
running = False

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
    start(event)


