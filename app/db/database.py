from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base

DATABASE_URL = "postgresql://martin:Martin23@localhost/martin"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)
