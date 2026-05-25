from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGODB_URI, MONGODB_DB
import certifi
import logging

logger = logging.getLogger("vedora.db")

client: AsyncIOMotorClient | None = None
db = None


def connect_to_mongo():
    """Create an AsyncIOMotorClient with an explicit CA bundle to avoid
    SSL handshake errors in some hosting environments (e.g. Render).

    Uses certifi.where() for the CA file, and increases serverSelectionTimeoutMS.
    """
    global client, db
    try:
        client = AsyncIOMotorClient(
            MONGODB_URI,
            tls=True,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=30000,
        )
        db = client[MONGODB_DB]
        # trigger a server selection to fail fast if there is a problem
        client.admin.command('ping')
        logger.info("Connected to MongoDB (ping successful)")
    except Exception:
        logger.exception("Failed to connect to MongoDB")
        raise
    return client


def close_mongo_connection():
    global client
    if client:
        client.close()
