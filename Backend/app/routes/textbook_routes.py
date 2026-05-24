from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from ..database import db
from ..services.textbook_service import save_textbook_bytes, validate_pdf, UPLOAD_DIR
from ..models.textbook_model import textbook_document
from ..deps import get_current_user
from bson import ObjectId
import os

router = APIRouter(prefix="/textbooks", tags=["textbooks"])


@router.post('/upload')
async def upload_textbook(file: UploadFile = File(...), uploadedBy: str = None, board: str = None, grade: str = None, subject: str = None, bookTitle: str = None, user=Depends(get_current_user)):
    content = await file.read()
    if not validate_pdf(file.filename, content):
        raise HTTPException(status_code=400, detail='Only PDF files under size limit are allowed')
    metadata = textbook_document(bookTitle or file.filename, user.get('id'), board or '', grade or '', subject or '', file.filename)
    tid = await save_textbook_bytes(file.filename, content, metadata)
    return {'id': tid}


@router.get('/')
async def list_textbooks():
    items = []
    cursor = db.textbooks.find({})
    async for t in cursor:
        t['id'] = str(t['_id'])
        items.append(t)
    return items


@router.get('/{textbookId}')
async def get_textbook(textbookId: str):
    t = await db.textbooks.find_one({'_id': ObjectId(textbookId)})
    if not t:
        raise HTTPException(status_code=404, detail='Not found')
    t['id'] = str(t['_id'])
    return t


@router.post('/{textbookId}/process')
async def process_textbook(textbookId: str, user=Depends(get_current_user)):
    # dummy processing: mark READY and add dummy chapters
    t = await db.textbooks.find_one({'_id': ObjectId(textbookId)})
    if not t:
        raise HTTPException(status_code=404, detail='Not found')
    # simulate extraction
    chapters = [
        {'title': 'Chapter 1 - Introduction', 'pageStart': 1},
        {'title': 'Chapter 2 - Basics', 'pageStart': 12},
        {'title': 'Chapter 3 - Advanced Topics', 'pageStart': 48},
    ]
    await db.textbooks.update_one({'_id': ObjectId(textbookId)}, {'$set': {'processingStatus': 'READY', 'chaptersExtracted': True, 'extractedText': '...', 'chapters': chapters}})
    return {'ok': True, 'chapters': chapters}


@router.delete('/{textbookId}')
async def delete_textbook(textbookId: str, user=Depends(get_current_user)):
    t = await db.textbooks.find_one({'_id': ObjectId(textbookId)})
    if not t:
        raise HTTPException(status_code=404, detail='Not found')
    # delete file
    fileUrl = t.get('fileUrl')
    if fileUrl and os.path.exists(fileUrl):
        os.remove(fileUrl)
    await db.textbooks.delete_one({'_id': ObjectId(textbookId)})
    return {'ok': True}
