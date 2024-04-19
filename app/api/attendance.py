from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.schemas.schemas import AttendanceCreate
from app.db.database import SessionLocal
from app.models.models import Attendance as AttendanceModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/mark-attendance/")
async def mark_attendance(attendance_data: AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = AttendanceModel(**attendance_data.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@router.get("/attendance/")
async def get_attendance(class_id: int, student_id: int = None, db: Session = Depends(get_db)):
    if student_id:
        attendance_records = db.query(AttendanceModel).filter(
            AttendanceModel.class_id == class_id,
            AttendanceModel.student_id == student_id
        ).all()
    else:
        attendance_records = db.query(AttendanceModel).filter(
            AttendanceModel.class_id == class_id
        ).all()
    if not attendance_records:
        raise HTTPException(status_code=404, detail="Attendance records not found")
    return attendance_records

@router.get("/attendance-report/")
async def generate_attendance_report(class_id: int, start_date: date, end_date: date, db: Session = Depends(get_db)):
    attendance_records = db.query(AttendanceModel).filter(
        AttendanceModel.class_id == class_id,
        AttendanceModel.date >= start_date,
        AttendanceModel.date <= end_date
    ).all()
    if not attendance_records:
        raise HTTPException(status_code=404, detail="No attendance records found for the specified criteria")
    total_classes = len(attendance_records)
    total_present = sum(1 for record in attendance_records if record.is_present)
    total_absent = total_classes - total_present
    attendance_summary = {
        "total_classes": total_classes,
        "total_present": total_present,
        "total_absent": total_absent,
        "attendance_percentage": (total_present / total_classes) * 100 if total_classes > 0 else 0
    }
    return attendance_summary
