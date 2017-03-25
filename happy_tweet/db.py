from pymongo import MongoClient

client = MongoClient()
db = client['test_db']


def insert(value, collection):
    col = db[collection]
    insert_id = col.update({'_id': value['_id']}, value, upsert=True)
    return insert_id


def get_all(collection):
    pass
