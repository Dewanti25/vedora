"""
Create a demo user in MongoDB using the same password hashing used by the app.

Run with:
  .\venv\Scripts\Activate.ps1
  python scripts\create_demo_user.py

This script reads `Backend/.env` for `MONGODB_URI` and will insert or update
the demo user `demo@vedora.test` with password `Demo@123`.
"""
from pymongo import MongoClient
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(MONGODB_URI)
db = client.get_database('vedora')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_demo_user(email: str = 'demo@vedora.test', password: str = 'Demo@123'):
    hashed = hash_password(password)
    user = db.users.find_one({'email': email})
    if user:
        db.users.update_one({'email': email}, {'$set': {'password': hashed, 'role': 'student'}})
        print(f'Updated demo user {email}')
    else:
        db.users.insert_one({'email': email, 'password': hashed, 'role': 'student'})
        print(f'Created demo user {email}')

if __name__ == '__main__':
    create_demo_user()
