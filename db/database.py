import sqlite3

DB_NAME = "tasks.db"


# 1. recommended to use context managers `with` for resource clean up
# 2. no error handling

def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()
