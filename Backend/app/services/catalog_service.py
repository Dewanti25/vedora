from ..database import db

async def create_entity(collection: str, doc: dict):
    res = await getattr(db, collection).insert_one(doc)
    return str(res.inserted_id)

async def list_entities(collection: str, filters: dict = None):
    items = []
    cursor = getattr(db, collection).find(filters or {})
    async for it in cursor:
        it['id'] = str(it['_id'])
        items.append(it)
    return items
