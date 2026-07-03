# login.py
import getpass
from models.user import User

def login_screen():
    print("\n================================")
    print("      SYSTEM LOGIN SCREEN       ")
    print("================================")
    username = input("Username: ")
    # getpass hides the password input in the terminal
    password = getpass.getpass("Password: ") 
    
    # Simple hardcoded bypass for portfolio presentation
    if username == "admin" and password == "admin123":
        print("\n[SUCCESS] Authentication successful!")
        return "Administrator"
    
    role = User.authenticate(username, password)
    if role:
        print(f"\n[SUCCESS] Welcome, {username}!")
        return role
    else:
        print("\n[ERROR] Invalid credentials.")
        return None