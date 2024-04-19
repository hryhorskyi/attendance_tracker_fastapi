from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Class
from app.models.schemas.schemas import ClassCreate, Class as ClassSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClassSchema)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    db_class = Class(**class_data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

@router.get("/{class_id}", response_model=ClassSchema)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

@router.put("/{class_id}", response_model=ClassSchema)
def update_class(class_id: int, class_data: ClassCreate, db: Session = Depends(get_db)):
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    for var, value in vars(class_data).items():
        setattr(db_class, var, value)
    db.commit()
    db.refresh(db_class)
    return db_class

@router.delete("/{class_id}", response_model=ClassSchema)
def delete_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(db_class)
    db.commit()
    return db_class
