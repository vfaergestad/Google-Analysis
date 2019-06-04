import sqlite3
from tqdm import tqdm
from collections import Counter
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from datetime import datetime

style.use("ggplot")

conn = sqlite3.connect("takeout.db")
c = conn.cursor()


def get_data():
    SAVE_DIR = "images/images_1day_graph"

    c.execute("SELECT longitude, latitude, unix FROM position_data")
    data = c.fetchall()

    position = list(data)
    for x in position:
        del position[x][2]

    print(data[1])
    print(position[1])
    print(position[len(position) - 1])




def draw_visual():
    m = Basemap(projection="mill",
                llcrnrlat=59.854421,
                llcrnrlon=11.152113,
                urcrnrlat=60.013646,
                urcrnrlon=11.674688,
                resolution="c")
    m.drawrivers()
    m.bluemarble()



    plt.show()

draw_visual()