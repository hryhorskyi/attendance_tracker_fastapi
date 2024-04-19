from fastapi import FastAPI
from typing import Union

from app.db.database import create_tables
from app.models.schemas.schemas import StudentCreate


app = FastAPI()

create_tables()

@app.post("/students/")
async def create_student(student: StudentCreate):
    # Validate and process the incoming data
    return {"name": student.name, "email": student.email}

