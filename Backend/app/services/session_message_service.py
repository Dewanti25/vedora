from ..database import db
from bson import ObjectId
from ..models.session_message_model import session_message_document


async def save_message(sessionId: str, message: str, senderType: str = 'STUDENT', studentId: str = None, messageType: str = 'TEXT'):
    doc = session_message_document(sessionId, message, senderType=senderType, studentId=studentId, messageType=messageType)
    res = await db.session_messages.insert_one(doc)
    return str(res.inserted_id)


async def list_messages(sessionId: str):
    items = []
    cursor = db.session_messages.find({'sessionId': sessionId}).sort('createdAt', 1)
    async for m in cursor:
        m['id'] = str(m['_id'])
        items.append(m)
    return items


async def generate_ai_response(sessionId: str, prompt: str):
    # dummy AI response generator
    ai_text = f"AI: I received your question: {prompt}. Here's a helpful hint to get you started."
    # save AI message
    res = await db.session_messages.insert_one({'sessionId': sessionId, 'senderType': 'AI', 'message': ai_text, 'messageType': 'TEXT'})
    return {'id': str(res.inserted_id), 'message': ai_text}
