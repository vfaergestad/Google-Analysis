import sqlite3
from tqdm import tqdm
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from datetime import datetime

style.use("ggplot")

conn = sqlite3.connect("takeout.db")
c = conn.cursor()


def position_visual():
    SAVE_DIR = "images/images_1day_graph"

    c.execute("SELECT longitude, latitude, unix FROM position_data")
    data = c.fetchall()

    position = list(data)
    for x in position:
        del position[x][2]

    print(data[1])
    print(position[1])
    print(position[len(position) - 1])





position_visual()
