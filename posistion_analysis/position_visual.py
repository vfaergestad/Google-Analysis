import sqlite3
from tqdm import tqdm
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from datetime import datetime

style.use("ggplot")

conn = sqlite3.connect("D:/Biblioteker/Dokumenter/GitHub/Google-Analysis/takeout.db")
c = conn.cursor()


def position_visual():
    SAVE_DIR = "images/images_1day_graph"

    c.execute("SELECT max(unix) FROM position_data")
    max_time = c.fetchall()[0][0]

    c.execute("SELECT min(unix) FROM position_data")
    min_time = c.fetchall()[0][0]

    counter = 0

    c.execute(f"SELECT longitude, latitude FROM position_data WHERE unix > {START} and unix < {END}")
    data = c.fetchall()


    position = [i for i in data]




position_visual()
