from fastapi import FastAPI
from app.api import attendance, student, university_class

app = FastAPI()

app.include_router(attendance.router, prefix="/attendance")
app.include_router(student.router, prefix="/students")
app.include_router(university_class.router, prefix="/classes")
