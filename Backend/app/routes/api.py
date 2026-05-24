from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from typing import List
from ..database import db
from ..deps import get_current_user, admin_required
from ..schemas.batch import BatchCreate
from bson import ObjectId
import os
from datetime import datetime, date

router = APIRouter(prefix="/api", tags=["api"])


def _ensure_db():
    if db is None:
        raise HTTPException(status_code=500, detail="Database not available")


@router.post('/admin/batches')
async def create_batch(batch: BatchCreate, _=Depends(admin_required)):
    _ensure_db()
    doc = {
        'board': batch.board,
        'class': batch.class_grade,
        'subject': batch.subject,
        'name': batch.name,
        'max': batch.max_students,
        'students': 0,
        'start_date': batch.start_date,
        'days': batch.days or [],
        'start_time': batch.start_time,
        'end_time': batch.end_time,
        'createdAt': datetime.utcnow()
    }
    res = await db.batches.insert_one(doc)
    doc['_id'] = res.inserted_id
    return {'id': str(res.inserted_id)}


@router.get('/batches')
async def list_batches():
    _ensure_db()
    items = []
    cursor = db.batches.find({})
    async for b in cursor:
        b['id'] = str(b['_id'])
        items.append(b)
    return items


@router.post('/batches/{batch_id}/join')
async def join_batch(batch_id: str, user=Depends(get_current_user)):
    _ensure_db()
    # find batch
    batch = await db.batches.find_one({'_id': ObjectId(batch_id)})
    if not batch:
        raise HTTPException(status_code=404, detail='Batch not found')
    # check capacity
    if batch.get('students',0) >= batch.get('max',15):
        raise HTTPException(status_code=400, detail='Batch full')
    # create enrollment
    enrollment = {
        'user_email': user.get('email'),
        'user_id': user.get('id') or str(user.get('_id')),
        'batch_id': batch_id,
        'joinedAt': datetime.utcnow()
    }
    await db.enrollments.insert_one(enrollment)
    await db.batches.update_one({'_id': ObjectId(batch_id)}, {'$inc': {'students': 1}})
    return {'ok': True}


@router.post('/schools/classrooms')
async def create_classroom(board: str = Form(...), class_grade: str = Form(...), subject: str = Form(...), title: str = Form(...), file: UploadFile = File(None)):
    _ensure_db()
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    filename = None
    if file:
        filename = f"{int(datetime.utcnow().timestamp())}_{file.filename}"
        path = os.path.join(uploads_dir, filename)
        with open(path, 'wb') as f:
            content = await file.read()
            f.write(content)

    doc = {
        'board': board,
        'class': class_grade,
        'subject': subject,
        'title': title,
        'fileName': filename,
        'createdAt': datetime.utcnow()
    }
    res = await db.classrooms.insert_one(doc)
    return {'id': str(res.inserted_id)}


@router.get('/classrooms')
async def list_classrooms():
    _ensure_db()
    items = []
    cursor = db.classrooms.find({})
    async for c in cursor:
        c['id'] = str(c['_id'])
        items.append(c)
    return items


@router.post('/schedules')
async def create_schedule(batch_id: str, sessions: List[dict]):
    _ensure_db()
    doc = {'batch_id': batch_id, 'sessions': sessions, 'createdAt': datetime.utcnow()}
    res = await db.schedules.insert_one(doc)
    return {'id': str(res.inserted_id)}


@router.get('/sessions/today')
async def sessions_today(user=Depends(get_current_user)):
    _ensure_db()
    # find user enrollments
    enrolls = db.enrollments.find({'user_email': user.get('email')})
    batch_ids = []
    async for e in enrolls:
        batch_ids.append(e['batch_id'])

    today_str = date.today().isoformat()
    result = []
    cursor = db.schedules.find({'sessions.date': today_str})
    async for s in cursor:
        for sess in s.get('sessions', []):
            if sess.get('date') == today_str and sess.get('batch_id') in batch_ids:
                result.append(sess)
    return result


@router.post('/ai/sessions/{session_id}/complete')
async def complete_session(session_id: str, user=Depends(get_current_user)):
    _ensure_db()
    # record progress
    doc = {
        'session_id': session_id,
        'user_email': user.get('email'),
        'completedAt': datetime.utcnow()
    }
    await db.progress.insert_one(doc)
    return {'ok': True}
