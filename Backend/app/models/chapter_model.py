def chapter_document(course_id: str, title: str, order: int = 0):
    return {'course_id': course_id, 'title': title, 'order': order, 'createdAt': None}
