from ..database import db

async def create_notification(user_id: str, title: str, body: str):
    doc = {'user_id': user_id, 'title': title, 'body': body, 'read': False}
    res = await db.notifications.insert_one(doc)
    return str(res.inserted_id)
