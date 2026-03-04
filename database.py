import sqlite3
from config import DB_PATH, DATA_DIR

def init_db():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS mails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account TEXT,
        sender TEXT,
        subject TEXT,
        date TEXT,
        file_path TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()


def insert_mail(account, sender, subject, date, file_path):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO mails
    (account, sender, subject, date, file_path)
    VALUES (?, ?, ?, ?, ?)
    """, (account, sender, subject, date, file_path))

    conn.commit()
    conn.close()
