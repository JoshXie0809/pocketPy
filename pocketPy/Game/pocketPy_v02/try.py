import Playing
import os
import numpy as np
import pandas as pd
from json import dumps, loads

playerDF = pd.read_json("./data/player/player.json")
print(playerDF.iloc[5,1], playerDF.iloc[6,1])
