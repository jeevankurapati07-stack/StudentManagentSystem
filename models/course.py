# models/course.py
from database import get_connection

class Course:
    def __init__(self, course_name, department, credits, faculty_id=None, course_id=None):
        self.course_id = course_id
        self.course_name = course_name
        self.department = department
        self.credits = credits
        self.faculty_id = faculty_id

    def add_course(self):
        print(f"[SUCCESS] Course {self.course_name} created. (Database query simulated)")