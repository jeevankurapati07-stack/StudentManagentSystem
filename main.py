# main.py
import sys
from database import initialize_database
from login import login_screen
from models.student import Student
from models.faculty import Faculty
from models.course import Course

def dashboard(role):
    while True:
        print("\n================================")
        print("      STUDENT MANAGEMENT      ")
        print(f"      Role: {role.upper()}    ")
        print("================================")
        print("1. Add Student (Demo)")
        print("2. Add Faculty (Demo)")
        print("3. Add Course (Demo)")
        print("4. Logout")
        print("================================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            s = Student("John Doe", "john@edu.com", "555-1234", "M", "Computer Science", 2, 3.8)
            s.add_student()
        elif choice == '2':
            f = Faculty("Dr. Smith", "Computer Science", "Professor", "smith@edu.com", "555-9876")
            f.add_faculty()
        elif choice == '3':
            c = Course("Data Structures", "Computer Science", 4)
            c.add_course()
        elif choice == '4':
            print("Logging out... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    initialize_database()
    
    role = login_screen()
    if role:
        dashboard(role)
    else:
        print("Exiting application...")