import sqlite3

DATABASE_NAME = "DBgame.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS player(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT UNIQUE NOT NULL,
                Stage INTEGER DEFAULT 1,
                Action INTEGER DEFAULT 0
            )""",

        """CREATE TABLE IF NOT EXISTS literals(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT UNIQUE NOT NULL,
                Data TEXT NOT NULL)
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
