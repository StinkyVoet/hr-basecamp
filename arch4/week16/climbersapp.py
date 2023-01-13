import os
import sys
import json
import sqlite3

from climber import Climber
from mountain import Mountain
from expedition import Expedition


def needs_import(cur: sqlite3.Cursor):
    result = cur.execute("SELECT * FROM climbers LIMIT 1")
    return not result.fetchall()


def import_data(con: sqlite3.Connection, cur: sqlite3.Cursor):
    with open("expeditions.json") as f:
        data: list[dict] = json.load(f)

    # parse into seperate sets
    mountains = []
    climbers = []
    expeditions = []
    for i, expedition in enumerate(data):
        mountains.append(
            {
                "id": i,
                "name": expedition["mountain"]["name"],
                "country": expedition["mountain"]["countries"][0],
                "rank": expedition["mountain"]["rank"],
                "height": expedition["mountain"]["height"],
                "prominence": expedition["mountain"]["prominence"],
                "range": expedition["mountain"]["range"],
            }
        )

        for exped_climbers in expedition["climbers"]:
            climbers.append(
                {
                    "id": exped_climbers["id"],
                    "first_name": exped_climbers["first_name"],
                    "last_name": exped_climbers["last_name"],
                    "nationality": exped_climbers["nationality"],
                    "date_of_birth": exped_climbers["date_of_birth"],
                }
            )

        expeditions.append(
            {
                "id": expedition["id"],
                "name": expedition["name"],
                "start": expedition["start"],
                "date": expedition["date"],
                "country": expedition["country"],
                "duration": expedition["duration"],
                "success": expedition["success"],
                "mountain_name": expedition["mountain"]["name"],
            }
        )

    # filter duplicate entries and convert the list of dicts to a list of lists so it can be used in the `executemany()` function
    mountains = [
        list(col.values()) for col in list({v["name"]: v for v in mountains}.values())
    ]
    climbers = [
        list(col.values()) for col in list({v["id"]: v for v in climbers}.values())
    ]

    # insert data into database
    cur.executemany("INSERT INTO mountains VALUES (?, ?, ?, ?, ?, ?, ?)", mountains)
    cur.executemany("INSERT INTO climbers VALUES (?, ?, ?, ?, ?)", climbers)
    con.commit()

    # revisit expeditions for mountain id's
    mountains = cur.execute("SELECT id,name FROM mountains").fetchall()

    for expedition in expeditions:
        for mountain in mountains:
            if expedition["mountain_name"] == mountain[1]:
                expedition["mountain_id"] = mountain[0]
                del expedition["mountain_name"]
                break

    expeditions = [list(col.values()) for col in expeditions]

    cur.executemany(
        "INSERT INTO expeditions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", expeditions
    )
    con.commit()


def main():
    con = sqlite3.connect("climbersapp.db")
    cur = con.cursor()

    if needs_import(cur):
        print("Tables are empty. Importing data...")
        import_data(con, cur)
    else:
        print("Tables have data. Skipping import")


if __name__ == "__main__":
    main()
