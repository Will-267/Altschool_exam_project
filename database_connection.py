from pymongo import MongoClient


client = MongoClient ('mongodb://localhost:27017/')
db = client["ecommerce"]

customers = db["customers"]
products = db["products"]
orders = db["orders"]
order_item = db["order_item"]

collection_names = db.list_collection_names()
print(collection_names)



