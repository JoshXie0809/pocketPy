def Start(filepath, event, screen, font, runningTime, screenSize=(480, 360), imgSize=(240, 240), startFontSize=24 ):
    """prepare start screen :
    needs :
    directory <- os.path.abspath('./')
    event <- pygame.event.get
    screen <- pygame.display.set_mode()
    font <- start Text 
    running time <- move space ~space~
    """
    from pygame import image, transform, KEYDOWN, K_SPACE
    rawstartImg = image.load(filepath)
    startImg = transform.scale(rawstartImg, imgSize)
    startImgPlace = ((screenSize[0] - startImg.get_width()) // 2, 
                     (screenSize[1] - startImg.get_height()) // 2 * 0.7)
    screen.blit(startImg, startImgPlace)

    startText = font.render("Pressed" + int(runningTime)%5  * " " + "~SPACE~" + (5 - int(runningTime)%5) * " " + "to Go", 
                            True, (0, 0, 0))
    startTextPlace = ((screenSize[0] - startText.get_width()) // 2, 5 / 3 * (screenSize[1] - startText.get_height()) // 2)
    screen.blit(startText, startTextPlace)

    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            print(f"!!!!START!!!!\n"
                  f"Time : {runningTime}")
            return 1
    return 0
