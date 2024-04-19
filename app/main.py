from fastapi import FastAPI
from app.api import attendance, student, university_class
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

app = FastAPI(title="Attendance tracker API Service")

app.include_router(attendance.router, prefix="/attendance")
app.include_router(student.router, prefix="/students")
app.include_router(university_class.router, prefix="/classes")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="/path/to/your/ssl/key.pem",
        ssl_certfile="/path/to/your/ssl/cert.pem",
    )