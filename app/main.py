from fastapi import FastAPI
from typing import Union

from app.db.database import create_tables

app = FastAPI()

create_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
