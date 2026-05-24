from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
MONGODB_DB = os.getenv('MONGODB_DB', 'Vedora')
JWT_SECRET = os.getenv('JWT_SECRET', 'change-me')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')
