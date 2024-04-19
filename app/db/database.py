from sqlalchemy import create_engine
from app.models.models import Base

DATABASE_URL = "postgresql://martin:Martin23@localhost/martin"
engine = create_engine(DATABASE_URL)

def create_tables():
    Base.metadata.create_all(bind=engine)
