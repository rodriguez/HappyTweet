from pymongo import MongoClient

client = MongoClient()
db = client['test_db']


def insert(value, collection):
    col = db[collection]
    insert_id = col.insert_one(value)
    return insert_id


def get_all(collection):
    return
