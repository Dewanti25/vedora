from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('MONGODB_URI')
print('Using URI:', uri)
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
try:
    info = client.server_info()
    print('Connected. MongoDB version:', info.get('version'))
    print('Databases:', client.list_database_names()[:10])
except Exception as e:
    print('Connection failed:', type(e).__name__, str(e))
