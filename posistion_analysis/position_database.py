import sqlite3
from tqdm import tqdm
import json

POSITION_DATA = "D:/Biblioteker/Dokumenter/gdata/Takeout/Posisjonslogg/Posisjonslogg.json"

conn = sqlite3.connect("D:/Biblioteker/Dokumenter/GitHub/Google-Analysis/takeout.db")
c = conn.cursor()


def make_table():
    c.execute("CREATE TABLE IF NOT EXISTS position_data(id INTEGER PRIMARY KEY, unix REAL, latitude INTEGER, "
              "longitude INTEGER, accuracy INTEGER, velocity INTEGER, heading INTEGER, altitude INTEGER, "
              "vertical_accuracy INTEGER)")


def position_data():
    data = json.load((open(POSITION_DATA)))

    for item in tqdm(data['locations']):
        try:
            timestamp = int(item['timestampMs'])
            latitude = item['latitudeE7']
            longitude = item['longitudeE7']
            accuracy = item['accuracy']
            if 'velocity' in item:
                velocity = item['velocity']
            else:
                velocity = 0

            if 'heading' in item:
                heading = item['heading']
            else:
                heading = 0

            if 'altitude' in item:
                altitude = item['altitude']
            else:
                altitude = 0

            if 'verticalAccuracy' in item:
                vertical_accuracy = item['verticalAccuracy']
            else:
                vertical_accuracy = 0

            c.execute("INSERT INTO position_data (unix, latitude, longitude, accuracy, velocity, heading, "
                      "altitude, vertical_accuracy) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (timestamp, latitude, longitude,
                                                                                       accuracy, velocity,
                                                                                       heading, altitude,
                                                                                       vertical_accuracy))
        except Exception as e:
            print(str(e))


make_table()
position_data()

conn.commit()
conn.close()

