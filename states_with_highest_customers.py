from database_connection import db
from pymongo import MongoClient

pipeline = [
    {
        '$group': { 
            '_id': '$address.state', 
            'customer_count': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'customer_count': -1
        }
    }, {
        '$limit': 3
    }
]
result = list(db.customers.aggregate(pipeline))
print("Sates with the highest number of customers:")
for item in result:
    print(f"State: {item['_id']}, Number of Customers: {item['customer_count']}")
    