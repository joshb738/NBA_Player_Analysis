from fastapi import FastAPI

from app.server.routes.nba import router as NBARouter

app = FastAPI()

app.include_router(NBARouter, tags=["api"], prefix="/api")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "FastAPI is alive"}
