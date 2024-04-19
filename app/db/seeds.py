from datetime import date
from sqlalchemy.orm import Session
from app.models.models import Student, Class, Attendance
from app.db.database import SessionLocal

def seed_data():
    db = SessionLocal()
    try:
        student1 = Student(name="Alice", email="alice@example.com")
        student2 = Student(name="Bob", email="bob@example.com")
        
        class1 = Class(name="Math 101", code="MATH101")
        class2 = Class(name="History 101", code="HIST101")
        
        attendance1 = Attendance(student_id=1, class_id=1, date=date.today(), is_present=True)
        attendance2 = Attendance(student_id=2, class_id=2, date=date.today(), is_present=False)
        
        db.add_all([student1, student2, class1, class2, attendance1, attendance2])
        
        db.commit()
    except Exception as e:
        print("Failed to seed database:", e)
        db.rollback()
    finally:
        db.close()
