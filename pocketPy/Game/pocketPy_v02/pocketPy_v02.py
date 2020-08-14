import pygame
import sys
import numpy as np
import pandas as pd
import os

from pocketPy_v02_ToolBox.Start import Start

localPath = os.path.abspath('../')
print('\n' + localPath)

iconImg = pygame.transform.scale(pygame.image.load(localPath + '/ball.png'), (27, 27))
pygame.display.set_icon(iconImg)
pygame.display.set_caption('pocketPy v0.2')
pygame.init()
pygame.font.init()


fontSize = 24
font = pygame.font.SysFont("comicsansms", fontSize)
clock = pygame.time.Clock()
screenSize = (480, 360)
screen = pygame.display.set_mode(screenSize)

running = True
stage = 0
# while loop
while running:
    clock.tick(50)  # 1 sec 50 frames
    # print(clock.get_time())
    runningTime = pygame.time.get_ticks() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(f"End time : {runningTime} sec")

    if stage == 0:
        screen.fill((255, 255, 255))
        stage = Start(localPath + '/start.png', event, screen, font, runningTime=runningTime,
                      screenSize=screenSize, imgSize=(200, 200), startFontSize=fontSize)
    if stage == 1:
        screen.fill((0, 0, 0))

    pygame.display.update()
# while loop

pygame.font.quit()
pygame.quit()
