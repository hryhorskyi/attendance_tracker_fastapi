from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String, unique=True)

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    class_id = Column(Integer, ForeignKey('classes.id'))
    date = Column(Date)
    is_present = Column(Boolean)

    student = relationship('Student', backref='attendances')
    class_obj = relationship('Class', backref='attendances')
