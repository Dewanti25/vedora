from ..database import db
from bson import ObjectId


async def create_schedule(batchId: str, payload: dict):
    doc = payload.copy()
    doc['batchId'] = batchId
    res = await db.schedules.insert_one(doc)
    return str(res.inserted_id)


async def get_schedules_for_batch(batchId: str):
    items = []
    cursor = db.schedules.find({'batchId': batchId})
    async for s in cursor:
        s['id'] = str(s['_id'])
        items.append(s)
    return items


async def get_schedule(scheduleId: str):
    return await db.schedules.find_one({'_id': ObjectId(scheduleId)})


async def update_schedule(scheduleId: str, payload: dict):
    await db.schedules.update_one({'_id': ObjectId(scheduleId)}, {'$set': payload})
    return True


async def delete_schedule(scheduleId: str):
    await db.schedules.delete_one({'_id': ObjectId(scheduleId)})
    return True


async def get_schedules_for_student(user):
    # find enrolled batch ids for this user
    user_id = user.get('id') or str(user.get('_id'))
    batch_ids = []
    cursor = db.enrollments.find({'user_id': user_id})
    async for e in cursor:
        batch_ids.append(e.get('batch_id'))

    items = []
    if not batch_ids:
        return items
    cursor = db.schedules.find({'batchId': {'$in': batch_ids}})
    async for s in cursor:
        s['id'] = str(s['_id'])
        items.append(s)
    return items
