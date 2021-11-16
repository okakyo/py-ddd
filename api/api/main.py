from fastapi import FastAPI
from sqlalchemy.orm.session import Session
from .presentations.controllers import user,chat,room

app = FastAPI()

app.include_router(user.router)
app.include_router(chat.router)
app.include_router(room.router)

@app.get("/")
async def root():
    return {"message": "Hello World !"}

@app.get("/health")
async def health_check(id):
  return "Good Healthy"
