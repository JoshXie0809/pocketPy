import pygame
import os

mainDir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = pygame.Rect(0, 0, 640, 480)


# load Img
def loadImg(filename):
    try:
        surface = pygame.image.load(os.path.join(mainDir, "Img", filename))
    except pygame.error:
        raise SystemExit('Could not load file')
    return surface.convert()


# initiate

pygame.init()
pygame.font.init()

pygame.font.quit()
pygame.quit()
