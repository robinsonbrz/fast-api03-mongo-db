import os
import os.path
from email.mime import application

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


if os.path.exists('.env'):
    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PASS = os.getenv('MONGODB_PASS')

client = MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@cluster0.0nnjfk0.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_app

collection_name = db["todos_app"]
