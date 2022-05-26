import os
import os.path
from multiprocessing import connection

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


MONGODB_USER = os.getenv('MONGODB_USER')
MONGODB_PASS = os.getenv('MONGODB_PASS')

connection_string = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@cluster0.0nnjfk0.mongodb.net/?retryWrites=true&w=majority"

print(connection_string)
client = MongoClient(connection_string)

db = client.todo_app

collection_name = db["todos_app"]
