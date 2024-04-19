from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str
    code: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True

class AttendanceBase(BaseModel):
    student_id: int
    class_id: int
    date: date
    is_present: bool

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int

    class Config:
        orm_mode = True
