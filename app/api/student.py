from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Student as StudentModel
from app.models.schemas.schemas import Student, StudentCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/students/", response_model=Student)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = StudentModel(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}
