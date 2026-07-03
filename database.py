# database.py
import sqlite3
import os
from config import Config

def get_connection():
    """
    Returns a database connection based on .env configuration.
    Currently defaults to SQLite for local development.
    """
    if Config.DB_TYPE == 'sqlite':
        os.makedirs(os.path.dirname(Config.SQLITE_PATH), exist_ok=True)
        return sqlite3.connect(Config.SQLITE_PATH)
    else:
        # Placeholder for MySQL/PostgreSQL logic
        print(f"Connecting to {Config.DB_TYPE} at {Config.DB_HOST}...")
        return None

def initialize_database():
    """Initializes tables using schema.sql."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as file:
                cursor.executescript(file.read())
                conn.commit()
                print("Database tables initialized successfully.")
        conn.close()