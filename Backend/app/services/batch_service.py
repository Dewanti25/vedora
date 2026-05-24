from ..database import db

async def create_batch(doc: dict):
    res = await db.batches.insert_one(doc)
    return str(res.inserted_id)

async def list_batches(filters: dict = None):
    items = []
    cursor = db.batches.find(filters or {})
    async for b in cursor:
        b['id'] = str(b['_id'])
        items.append(b)
    return items


async def join_batch_atomic(batch_id: str, user: dict):
    from bson import ObjectId
    # check existing enrollment
    existing = await db.enrollments.find_one({'user_id': user.get('id') or str(user.get('_id')), 'batch_id': batch_id})
    if existing:
        return {'status': 'already_enrolled'}

    # attempt to atomically increment students with a simple numeric compare
    batch_doc = await db.batches.find_one({'_id': ObjectId(batch_id)})
    if not batch_doc:
        return {'status': 'not_found'}
    max_students = batch_doc.get('max', 15)
    # try atomic increment
    updated = await db.batches.find_one_and_update({'_id': ObjectId(batch_id), 'students': {'$lt': max_students}}, {'$inc': {'students': 1}})
    if not updated:
        return {'status': 'full'}

    # create enrollment, but guard for duplicate key (race)
    enrollment = {
        'user_id': user.get('id') or str(user.get('_id')),
        'user_email': user.get('email'),
        'batch_id': batch_id,
        'joinedAt': __import__('datetime').datetime.utcnow()
    }
    try:
        await db.enrollments.insert_one(enrollment)
    except Exception as e:
        # handle duplicate key (user enrolled concurrently) or other DB errors
        from pymongo.errors import DuplicateKeyError
        if isinstance(e, DuplicateKeyError) or (hasattr(e, 'code') and getattr(e, 'code', None) == 11000):
            # rollback student count
            await db.batches.update_one({'_id': ObjectId(batch_id)}, {'$inc': {'students': -1}})
            return {'status': 'already_enrolled'}
        # rollback on generic failure
        await db.batches.update_one({'_id': ObjectId(batch_id)}, {'$inc': {'students': -1}})
        return {'status': 'error', 'error': str(e)}

    # create a notification and send an email (best-effort)
    try:
        from .notification_service import create_notification
        from .email_service import send_email
        await create_notification(enrollment['user_id'], 'Enrolled in batch', f"You have been enrolled in batch {batch_id}")
        await send_email(enrollment['user_email'], 'Vedora AI - Enrollment confirmed', f"You have been enrolled in batch {batch_id}.")
    except Exception:
        pass

    return {'status': 'enrolled'}
