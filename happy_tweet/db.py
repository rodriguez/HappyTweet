from pymongo import MongoClient

client = MongoClient()
db = client['test_db']


def insert(value, collection):
    col = db[collection]
    insert_id = col.update({'_id': value['_id']}, value, upsert=True)
    return insert_id


def search(key, collection):
    col = db[collection]
    data = col.find_one(key)
    return data


def search_many(key, collection):
    col = db[collection]
    data = col.find({"location": "Boston, Mass."})
    return [x for x in data]
