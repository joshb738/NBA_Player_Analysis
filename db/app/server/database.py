import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.players

players_collection = database.get_collection("nba_collection")


# Helpers
def player_helper(player) -> dict:
    return {
        "id": str(player["_id"]),
        "Year": player["Year"],
        "Player": player["Player"],
        "Age": player["Age"]
    }

# Retrieve all players present in the database


async def retrieve_players():
    players = []
    async for student in players_collection.find():
        players.append(player_helper(student))
    return players

# Retrieve a players with a matching ID


async def retrieve_player(id: str) -> dict:
    player = await players_collection.find_one({"_id": ObjectId(id)})
    if player:
        return player_helper(player)

# Add a new players into to the database


async def add_dataset(student_data: dict) -> dict:
    # Push all dataset to MongoDB
    player = await players_collection.insert_one(student_data)
    new_player = await players_collection.find_one({"_id": player.inserted_id})
    return player_helper(new_player)
