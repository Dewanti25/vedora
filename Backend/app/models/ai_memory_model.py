def ai_memory_document(user_id: str, context: dict) -> dict:
    return {
        'user_id': user_id,
        'context': context,
        'createdAt': None,
    }
