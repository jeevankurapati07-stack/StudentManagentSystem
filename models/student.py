# models/student.py
from database import get_connection

class Student:
    def __init__(self, name, email, phone, gender, department, year, cgpa, student_id=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.department = department
        self.year = year
        self.cgpa = cgpa

    def add_student(self):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO students (name, email, phone, gender, department, year, cgpa) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (self.name, self.email, self.phone, self.gender, self.department, self.year, self.cgpa))
            conn.commit()
            conn.close()
            print(f"[SUCCESS] Student {self.name} added to database.")