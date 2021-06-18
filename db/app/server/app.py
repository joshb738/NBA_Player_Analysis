from fastapi import FastAPI
import logging

# Import routes
from app.server.routes.nba import router as NBARouter

# App init
app = FastAPI()
logger = logging.getLogger("api")

# Route for API
app.include_router(NBARouter, tags=["api"], prefix="/api")

# General route for testing if online


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "FastAPI is alive"}
