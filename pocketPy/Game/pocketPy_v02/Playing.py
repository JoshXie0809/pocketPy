def Playing(filePath, screen, event):
    import numpy as np
    import pandas as pd
    import os
    from pygame import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, image, transform

    """change data at ./data/player/player.json"""

    os.chdir(filePath)
    playerDF = pd.read_json("./data/player/player.json")
    # load data




    playerImgSize = (20, 30)
    playerImg = {
                'down': [transform.scale(image.load('./image/player/fore.png'), playerImgSize),
                         transform.scale(image.load('./image/player/fore1.png'), playerImgSize),
                         transform.scale(image.load('./image/player/fore2.png'), playerImgSize)],
                'up': [transform.scale(image.load('./image/player/back.png'), playerImgSize),
                       transform.scale(image.load('./image/player/back1.png'), playerImgSize),
                       transform.scale(image.load('./image/player/back2.png'), playerImgSize)],
                'left': [transform.scale(image.load('./image/player/left.png'), playerImgSize),
                         transform.scale(image.load('./image/player/left1.png'), playerImgSize),
                         transform.scale(image.load('./image/player/left2.png'), playerImgSize)],
                'right': [transform.scale(image.load('./image/player/right.png'), playerImgSize),
                          transform.scale(image.load('./image/player/right1.png'), playerImgSize),
                          transform.scale(image.load('./image/player/right2.png'), playerImgSize)]
                }
    if event.type == KEYDOWN:
        if event.key == K_UP:
            playerDF.iloc[7, 1] = 'up'
    screen.blit(playerImg[playerDirection][0], (playerx, playery))

    playerDF.to_json("./data/player/player.json")
    return 1, playerDF