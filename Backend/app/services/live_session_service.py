from ..database import db
from bson import ObjectId


async def create_session(payload: dict, created_by: str = None):
    doc = payload.copy()
    doc['createdBy'] = created_by
    res = await db.live_sessions.insert_one(doc)
    return str(res.inserted_id)


async def get_session(sessionId: str):
    return await db.live_sessions.find_one({'_id': ObjectId(sessionId)})


async def add_participant(sessionId: str, user_id: str):
    await db.live_sessions.update_one({'_id': ObjectId(sessionId)}, {'$addToSet': {'participants': user_id}})
    return True


async def remove_participant(sessionId: str, user_id: str):
    await db.live_sessions.update_one({'_id': ObjectId(sessionId)}, {'$pull': {'participants': user_id}})
    return True


async def complete_session(sessionId: str, summary: str = None):
    await db.live_sessions.update_one({'_id': ObjectId(sessionId)}, {'$set': {'status': 'COMPLETED', 'summary': summary}})
    return True
