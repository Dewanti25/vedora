import os
from datetime import datetime
from ..database import db
from ..models.homework_model import homework_document

UPLOAD_DIR = os.path.join('uploads', 'homework')
MAX_FILE_SIZE = 25 * 1024 * 1024


def _ensure_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


async def assign_homework(batchId: str, title: str, description: str, subject: str, dueDate: str, sessionId: str = None):
    doc = homework_document(batchId=batchId, title=title, description=description, subject=subject, dueDate=dueDate, sessionId=sessionId)
    res = await db.homework.insert_one(doc)
    return str(res.inserted_id)


def save_homework_bytes(filename: str, content: bytes) -> str:
    _ensure_dir()
    safe = filename.replace('..', '')
    path = os.path.join(UPLOAD_DIR, safe)
    with open(path, 'wb') as f:
        f.write(content)
    return path


async def submit_homework(assignmentId: str, studentId: str, filename: str, content: bytes, extra: dict = None):
    file_path = save_homework_bytes(filename, content)
    # create a submission document linking to assignmentId via parentAssignmentId
    doc = homework_document(
        batchId=extra.get('batchId') if extra else '',
        title=extra.get('title') if extra else '',
        description=extra.get('description') if extra else '',
        subject=extra.get('subject') if extra else '',
        dueDate=extra.get('dueDate') if extra else '',
        sessionId=extra.get('sessionId') if extra else None,
        studentId=studentId,
        fileUrl=file_path,
        status='SUBMITTED',
        submittedAt=datetime.utcnow(),
    )
    # store parentAssignmentId for reference
    if extra and extra.get('assignmentId'):
        doc['parentAssignmentId'] = extra.get('assignmentId')
    res = await db.homework.insert_one(doc)
    return str(res.inserted_id)


async def list_my_homework(studentId: str):
    items = []
    cursor = db.homework.find({'studentId': studentId})
    async for h in cursor:
        h['id'] = str(h['_id'])
        items.append(h)
    return items


async def list_batch_homework(batchId: str):
    items = []
    cursor = db.homework.find({'batchId': batchId})
    async for h in cursor:
        h['id'] = str(h['_id'])
        items.append(h)
    return items


async def evaluate_homework(homeworkId: str, marks: float = None, feedback: str = None, status: str = 'EVALUATED'):
    from bson import ObjectId
    update = {'status': status}
    if marks is not None:
        update['marks'] = marks
    if feedback is not None:
        update['feedback'] = feedback
    update['evaluatedAt'] = datetime.utcnow()
    await db.homework.update_one({'_id': ObjectId(homeworkId)}, {'$set': update})
    return True


async def delete_homework(homeworkId: str):
    # find and delete
    try:
        from bson import ObjectId
        h = await db.homework.find_one({'_id': ObjectId(homeworkId)})
    except Exception:
        h = None
    if not h:
        return False
    fileUrl = h.get('fileUrl')
    if fileUrl and os.path.exists(fileUrl):
        os.remove(fileUrl)
    await db.homework.delete_one({'_id': ObjectId(homeworkId)})
    return True
