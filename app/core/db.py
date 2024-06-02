import sqlite3
from app.core.config import settings

def get_db_conn():
    conn = sqlite3.connect(settings.DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def startup_event():
    conn = get_db_conn()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL, is_offer INTEGER)"
    )
    conn.commit()