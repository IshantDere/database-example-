# main.py

from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import Base, engine, SessionLocal

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Integer)
    b = Column(Integer)
    result = Column(Integer)

import time
time.sleep(5)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class AddRequest(BaseModel):
    a: int
    b: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add")
def add_numbers(data: AddRequest, db: Session = Depends(get_db)):
    result = data.a + data.b
    calc = Calculation(a=data.a, b=data.b, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc