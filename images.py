import sqlite3
from tqdm import tqdm

conn = sqlite3.connect("takeout.db")
c = conn.cursor()

DAY = 86400
YEAR = 365 * DAY

SLIDE = 1 * DAY

def words_graph():
    SAVE_DIR = "images_1day_graph"

    c.execute("SELECT max(unix) FROM WORDS")
    max_time = c.fetchall()[0][0]

    c.execute("SELECT min(unix) FROM WORDS")
    min_time = c.fetchall()[0][0]
    print(min_time, max_time)

    START = min_time
    END = min_time + window

words_graph()
