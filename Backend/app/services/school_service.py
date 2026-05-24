from ..database import db

async def create_school(doc: dict):
    res = await db.schools.insert_one(doc)
    return str(res.inserted_id)

async def get_school(school_id: str):
    return await db.schools.find_one({'_id': school_id})

async def list_schools():
    items = []
    cursor = db.schools.find({})
    async for s in cursor:
        s['id'] = str(s['_id'])
        items.append(s)
    return items
