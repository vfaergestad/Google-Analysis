import sqlite3
from tqdm import tqdm
import dateutil.parser
from stopwords import stop_words

SEARCH_ACTIVITY = "D:/Biblioteker/Dokumenter/gdata/Takeout/Min aktivitet/Søk/MinAktivitet.html"

conn = sqlite3.connect("takeout.db")
c = conn.cursor()


def make_table():
    c.execute("CREATE TABLE IF NOT EXISTS words(id INTEGER PRIMARY KEY, unix REAL, word TEXT)")


def search_data():
    with open(SEARCH_ACTIVITY, "r", encoding="utf8") as f:
        content = f.read()
        for item in tqdm(content.split("Søkte etter")[1:]):
            try:
                search_string = item.split("\">")[1].split("</a>")[0]
                date_3 = item.split("<br>")[1].split("</div")[0]
                date_2 = date_3.replace("mai", "may")
                date_1 = date_2.replace("okt", "oct")
                date = date_1.replace("des", "dec")
                d = dateutil.parser.parse(date).timestamp()

                for w in search_string.split(" "):
                    if w not in stop_words:
                        c.execute("INSERT INTO words (unix, word) VALUES (?, ?)", (d, w))
            except Exception as e:
                print(str(e))


make_table()
search_data()

conn.commit()
conn.close()
