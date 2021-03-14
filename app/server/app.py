from fastapi import FastAPI
from .routes.audio import router as AudioRouter

app = FastAPI()
app.include_router(AudioRouter, tags=["Audio"], prefix="")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
