import os
from pymongo import MongoClient

MONGO_DATABASE_URL = os.environ.get("MONGO_DB_URL")

client = MongoClient(MONGO_DATABASE_URL)
client.dev.connect('ping')

ChatDB = client.dev
