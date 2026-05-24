def progress_document(user_id: str, batch_id: str, session_id: str, percent: float) -> dict:
    return {
        'user_id': user_id,
        'batch_id': batch_id,
        'session_id': session_id,
        'percent': percent,
        'updatedAt': None,
    }
