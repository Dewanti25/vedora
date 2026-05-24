from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGODB_URI, MONGODB_DB

client: AsyncIOMotorClient | None = None
db = None

def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[MONGODB_DB]
    return client

def close_mongo_connection():
    global client
    if client:
        client.close()
