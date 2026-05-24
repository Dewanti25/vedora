import os
from ..database import db

UPLOAD_DIR = os.path.join('uploads', 'textbooks')
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB

def _ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_textbook_bytes(filename: str, content: bytes, metadata: dict):
    _ensure_upload_dir()
    safe_name = filename.replace('..', '')
    path = os.path.join(UPLOAD_DIR, safe_name)
    with open(path, 'wb') as f:
        f.write(content)
    metadata['fileName'] = safe_name
    metadata['fileUrl'] = path
    metadata['fileSize'] = len(content)
    res = await db.textbooks.insert_one(metadata)
    return str(res.inserted_id)


def validate_pdf(filename: str, content: bytes) -> bool:
    if not filename.lower().endswith('.pdf'):
        return False
    if len(content) > MAX_FILE_SIZE:
        return False
    # basic PDF header check
    return content[:4] == b'%PDF'
