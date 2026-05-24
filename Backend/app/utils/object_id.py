from bson import ObjectId

def to_str(doc: dict) -> dict:
    if not doc:
        return doc
    doc['id'] = str(doc.get('_id'))
    return doc
