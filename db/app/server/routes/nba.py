from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_dataset,
    retrieve_player,
    retrieve_players,
)
from app.server.models.nba import (
    ErrorResponseModel,
    ResponseModel,
    PlayerSchema,
)

router = APIRouter()


@router.post("/add_dataset", response_description="Dataset data added into the database")
async def add_dataset(player: PlayerSchema = Body(...)):
    dataset = jsonable_encoder(dataset)
    new_dataset = await add_player(dataset)
    return ResponseModel(new_dataset, "Dataset added successfully.")
