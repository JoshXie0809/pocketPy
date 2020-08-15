import pygame
import os
import numpy as np
import pandas as pd

from Start import Start
from Playing import Playing


localPath = os.path.abspath('./')
print('\n' + localPath)

iconImg = pygame.transform.scale(pygame.image.load(localPath + '/image/setting/ball.png'), (32, 32))
pygame.display.set_icon(iconImg)
pygame.display.set_caption('pocketPy v0.2')
pygame.init()
pygame.font.init()


fontSize = 24
font = pygame.font.SysFont("comicsansms", fontSize)
clock = pygame.time.Clock()
screenSize = (480, 360)
screen = pygame.display.set_mode(screenSize)

playerData =None
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
            print(f'!!!!End!!!!\nEnd time : {runningTime} sec')

    if stage == 0:
        screen.fill((255, 255, 255))
        stage = Start(localPath + '/image/start/start.png', event, screen, font, runningTime=runningTime,
                      screenSize=screenSize, imgSize=(200, 200), startFontSize=fontSize)
    if stage == 1:
        screen.fill((255, 255, 255))
        stage, playerData = Playing(localPath)

    pygame.display.update()
# while loop

print(playerData)
pygame.font.quit()
pygame.quit()
