# models/user.py
from database import get_connection

class User:
    def __init__(self, username, password, role="Student"):
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def authenticate(username, password):
        """Authenticates a user from the database."""
        conn = get_connection()
        if not conn: return False
        
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        
        return result[0] if result else None