def session_document(batch_id: str, title: str, date: str, start_time: str) -> dict:
    return {
        'batch_id': batch_id,
        'title': title,
        'date': date,
        'start_time': start_time,
        'status': 'upcoming',
        'createdAt': None,
    }
