import os
from email.mime import application

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


# USER = os.getenv('MONGODB_USER')
# PASSW = os.getenv('MONGODB_PASS')

client = MongoClient(f"mongodb+srv://os.getenv('MONGODB_USER'):os.getenv('MONGODB_PASS')@cluster0.0nnjfk0.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_app

collection_name = db["todos_app"]
