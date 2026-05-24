import os
from ..database import db
from ..models.notes_model import notes_document

UPLOAD_DIR = os.path.join('uploads', 'notes')
MAX_FILE_SIZE = 25 * 1024 * 1024


def _ensure_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_note_bytes(filename: str, content: bytes) -> str:
    _ensure_dir()
    safe = filename.replace('..', '')
    path = os.path.join(UPLOAD_DIR, safe)
    with open(path, 'wb') as f:
        f.write(content)
    return path


async def upload_note(title: str, board: str, grade: str, subject: str, filename: str, content: bytes, uploadedBy: str):
    file_path = save_note_bytes(filename, content)
    doc = notes_document(title=title, board=board, grade=grade, subject=subject, fileUrl=file_path, fileType='', fileSize=len(content), uploadedBy=uploadedBy)
    res = await db.notes.insert_one(doc)
    return str(res.inserted_id)


async def list_notes(board: str = None, grade: str = None, subject: str = None, search: str = None):
    query = {}
    if board:
        query['board'] = board
    if grade:
        query['grade'] = grade
    if subject:
        query['subject'] = subject
    if search:
        query['title'] = {'$regex': search, '$options': 'i'}
    items = []
    cursor = db.notes.find(query)
    async for n in cursor:
        n['id'] = str(n['_id'])
        items.append(n)
    return items


async def get_note(noteId: str):
    from bson import ObjectId
    return await db.notes.find_one({'_id': ObjectId(noteId)})


async def delete_note(noteId: str):
    from bson import ObjectId
    n = await db.notes.find_one({'_id': ObjectId(noteId)})
    if not n:
        return False
    fileUrl = n.get('fileUrl')
    if fileUrl and os.path.exists(fileUrl):
        os.remove(fileUrl)
    await db.notes.delete_one({'_id': ObjectId(noteId)})
    return True
