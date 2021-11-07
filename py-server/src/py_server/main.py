from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def index():
	return "Hello World"

def main():
    uvicorn.run(app, host="0.0.0.0", port=5555, reload=True)

if __name__ == "__main__":
    main()
