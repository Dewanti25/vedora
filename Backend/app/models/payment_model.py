def payment_document(user_id: str, amount: float, currency: str = 'INR'):
    return {'user_id': user_id, 'amount': amount, 'currency': currency, 'status': 'pending', 'createdAt': None}
