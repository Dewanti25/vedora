def subscription_document(school_id: str, plan: str, status: str = 'active'):
    return {'school_id': school_id, 'plan': plan, 'status': status, 'createdAt': None}
