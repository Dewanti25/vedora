from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from ..deps import get_current_user
from ..services.notes_service import upload_note, list_notes, get_note, delete_note
from fastapi.responses import FileResponse
from typing import Optional

router = APIRouter(prefix="/notes", tags=["notes"])


def _role_allowed(user: dict):
    return user.get('role') in ('admin', 'school_admin', 'teacher')


@router.post('/upload')
async def upload(title: str = Form(...), board: Optional[str] = Form(None), grade: Optional[str] = Form(None), subject: Optional[str] = Form(None), file: UploadFile = File(...), user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    content = await file.read()
    if len(content) > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail='File too large')
    nid = await upload_note(title, board or '', grade or '', subject or '', file.filename, content, user.get('id'))
    return {'id': nid}


@router.get('/')
async def list_route(board: Optional[str] = None, grade: Optional[str] = None, subject: Optional[str] = None, search: Optional[str] = None, user=Depends(get_current_user)):
    items = await list_notes(board, grade, subject, search)
    for it in items:
        it['id'] = str(it['_id'])
    return items


@router.get('/{noteId}')
async def get_route(noteId: str, user=Depends(get_current_user)):
    n = await get_note(noteId)
    if not n:
        raise HTTPException(status_code=404, detail='Not found')
    n['id'] = str(n['_id'])
    return n


@router.get('/{noteId}/download')
async def download_route(noteId: str, user=Depends(get_current_user)):
    n = await get_note(noteId)
    if not n:
        raise HTTPException(status_code=404, detail='Not found')
    fileUrl = n.get('fileUrl')
    if not fileUrl:
        raise HTTPException(status_code=404, detail='File missing')
    return FileResponse(path=fileUrl, filename=n.get('fileName') or 'notes')


@router.delete('/{noteId}')
async def delete_route(noteId: str, user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    ok = await delete_note(noteId)
    if not ok:
        raise HTTPException(status_code=404, detail='Not found')
    return {'ok': True}
