import pygame
import sys

path = '/Users/xiezhengqi/Desktop/GitHub/pocketPy/pocketPy/Game'

pygame.display.set_caption('pocketPy mac ver0.0')
iconImg = pygame.image.load(path + '/ball.png')
pygame.display.set_icon(iconImg)
pygame.init()
screenSize = (480, 360)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()


# start function######################################################################################################
######################################################################################################
######################################################################################################
startImg = pygame.image.load(path + '/start.png')
startImgPlace = ((screenSize[0] - startImg.get_width()) // 2, 40)
startSpace1 = 0
startSpace2 = (startSpace1 // 25) % 6
font = pygame.font.SysFont("comicsansms", 25)
startText = font.render("Pressed" + startSpace2 * " " + "~SPACE~" + (6 - startSpace2) * " " + "to Go", True, (0, 0, 0))
startTextPlace = ((screenSize[0] - startText.get_width()) // 2, 5/3*(screenSize[1] - startText.get_height()) // 2)


def start():
    global startImg, startSpace1, startSpace2, startImgPlace, startText, startTextPlace
    startSpace1 = (startSpace1 + 1) % 150
    startSpace2 = (startSpace1 // 25) % 6
    startText = font.render("Pressed" + startSpace2 * " " + "~SPACE~" + (6 - startSpace2) * " " + "to Go", True,
                            (0, 0, 0))
    screen.blit(startImg, startImgPlace)
    screen.blit(startText, startTextPlace)
    pygame.display.update()



# player function ######################################################################################################
######################################################################################################
######################################################################################################
playerImg = pygame.image.load(path + '/player')

def player():
    pass

######################################################################################################
######################################################################################################
######################################################################################################


done = False
running = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = 1

        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
            sys.exit()
    # start page
    if running == 0:
        screen.fill((255, 255, 255))
        start()

    # gaming loop
    if running == 1:
        screen.fill((255, 255, 255))
    pygame.display.update()



