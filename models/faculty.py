# models/faculty.py
from database import get_connection

class Faculty:
    def __init__(self, name, department, designation, email, phone, faculty_id=None):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.designation = designation
        self.email = email
        self.phone = phone

    def add_faculty(self):
        print(f"[SUCCESS] Faculty {self.name} added. (Database query simulated)")