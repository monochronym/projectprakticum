from fastapi import FastAPI
import uvicorn
from api import api
app = FastAPI()

@app.get("/hello")
async def hello():
    return "hello"

app.include_router(api)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)