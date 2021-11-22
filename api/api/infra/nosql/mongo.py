from pymongo import MongoClient

client = MongoClient()
client.db_name.connect('ping')
