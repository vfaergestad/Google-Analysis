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

DAY = 86400
YEAR = 365 * DAY

SLIDE = 1 * DAY
WINDOW = 1 * YEAR

def words_graph():
    SAVE_DIR = "images_1day_graph"

    c.execute("SELECT max(unix) FROM WORDS")
    max_time = c.fetchall()[0][0]

    c.execute("SELECT min(unix) FROM WORDS")
    min_time = c.fetchall()[0][0]

    START = min_time
    END = min_time + WINDOW
    counter = 0

    while END < max_time:
        c.execute(f"SELECT word FROM words WHERE unix > {START} and unix < {END}")
        data = c.fetchall()

        words = [i[0] for i in data]

        word_counter = Counter(words)

        common_words = [topic[0] for topic in word_counter.most_common(10)]
        y_pos = np.arange(len(common_words))
        word_counts = [topic[1] for topic in word_counter.most_common(10)]

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



words_graph()
