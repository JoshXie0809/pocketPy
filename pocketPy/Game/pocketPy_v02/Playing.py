def Playing(filePath):
    import numpy as np
    import pandas as pd
    import os
    os.chdir(filePath)
    playerDF = pd.read_csv("./data/player/player.csv", sep=' ', index_col= 'index')

    return 1, playerDF