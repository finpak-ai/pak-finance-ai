import sqlite3
import os

# SQLite database path
DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")

def get_connection():
    """
    Returns a SQLite connection with a 10-second timeout.
    Always close the connection after use.
    """
    return sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)

def init_db():
    """
    Initialize transactions table if it doesn't exist
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT CHECK(type IN ('income','expense')) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    finally:
        conn.close()
