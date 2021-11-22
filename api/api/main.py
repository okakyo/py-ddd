from fastapi import FastAPI
from sqlalchemy.orm.session import Session
from .presentations.controllers import user,chat,room
from .infra.postgre.database import create_tables,SessionLocal
from typing import Iterator
import os 

app = FastAPI()

create_tables()

def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app.include_router(user.router)
app.include_router(chat.router)
app.include_router(room.router)

@app.get("/")
async def root():
    return {"message": "Hello World !"}

@app.get("/health")
async def health_check(id):
  return "Good Healthy"
