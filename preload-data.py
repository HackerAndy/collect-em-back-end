from pymongo import MongoClient
import json
import os
from datetime import datetime
import pytz
import sys

MONGO_URI = "mongodb://127.0.0.1:27017/BasementOfHolding?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client.get_default_database()

def load_data_into_query():
    with open('mongodb_data.json') as json_file:
        json_as_dictionary = json.load(json_file)
    return json_as_dictionary

def insert_many(query):
    # query["lastModified"] = datetime.now(pytz.UTC)
    query_with_timestamp = {}
    for collectible in query:
        query_with_timestamp = collectible
        query_with_timestamp['lastModified'] = datetime.now(pytz.UTC)


    db.myCollectibles.insert_many(query)

def delete_many(query):
    for collectible in query:
        db.myCollectibles.delete_one(collectible)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    query = load_data_into_query()
    if sys.argv[1] == 'insert':
        insert_many(query)
    if sys.argv[1] == 'delete':
        delete_many(query)
