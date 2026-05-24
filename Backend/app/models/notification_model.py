def notification_document(user_id: str, title: str, body: str):
    return {'user_id': user_id, 'title': title, 'body': body, 'read': False, 'createdAt': None}
