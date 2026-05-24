from pymongo import MongoClient
import os

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(MONGODB_URI)
db = client.get_database('vedora')

users = list(db.users.find({}, {'password':0}))
print('users_count=', len(users))
for u in users:
    u['_id'] = str(u['_id'])
    print(u)
