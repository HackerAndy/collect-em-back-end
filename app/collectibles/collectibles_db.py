from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
import os

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db
       
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def find_by_owner(owner_id, results_per_page):
    query = {}
    query["ownerId"] = owner_id

    try:
        collectible = db.myCollectibles.find(query).limit(results_per_page)
        total_records = db.myCollectibles.count_documents(query)
        return list(collectible), total_records
    except Exception as exception:
        return exception

if __name__ == "__main__":
  print(os.path.basename(__file__))