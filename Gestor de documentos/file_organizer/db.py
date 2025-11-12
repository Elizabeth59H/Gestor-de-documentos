import sqlite3
from datetime import datetime

DB_NAME = "organized_files.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            extension TEXT,
            original_path TEXT,
            new_path TEXT,
            modified_date TEXT,
            moved_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_movement(file_name, extension, original_path, new_path, modified_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO file_log (file_name, extension, original_path, new_path, modified_date, moved_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (file_name, extension, original_path, new_path, modified_date, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
