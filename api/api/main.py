from fastapi import FastAPI, params

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World !"}

@app.get("/{id}")
async def user(id):
  return {"message": f"hello {id}"}
