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

DAY = 86400000
YEAR = 365 * DAY

SLIDE = 1 * DAY
WINDOW = 1 * YEAR

def position_visual():
    SAVE_DIR = "images/images_1day_graph"

    c.execute("SELECT max(unix) FROM position_data")
    max_time = c.fetchall()[0][0]

    c.execute("SELECT min(unix) FROM position_data")
    min_time = c.fetchall()[0][0]

    START = min_time
    END = min_time + WINDOW
    counter = 0


    while END < max_time:
        c.execute(f"SELECT longitude, latitude FROM position_data WHERE unix > {START} and unix < {END}")
        data = c.fetchall()


        position = [i for i in data]

        position_counter = Counter(position)

        common_position = [topic[0] for topic in position_counter.most_common(10)]
        y_pos = np.arange(len(common_position))
        position_counts = [topic[1] for topic in position_counter.most_common(10)]

        print(common_position)
        exit()

        plt.figure(figsize=(12, 7))
        plt.bar(y_pos, word_counts, align="center", alpha=0.5)
        plt.xticks(y_pos, common_words)
        plt.ylabel("Volume")
        plt.title(f"{datetime.fromtimestamp(END).day}-{datetime.fromtimestamp(END).month}-{datetime.fromtimestamp(END).year}")
        plt.savefig(f"{SAVE_DIR}/{counter}.png")
        plt.close()

        counter += 1
        START += SLIDE
        END += SLIDE



position_visual()
