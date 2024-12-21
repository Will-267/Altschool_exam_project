from database_connection import db
from pymongo import MongoClient

pipeline = [
    {'$group': {'_id': "$category", "totalRevenue": {'$sum': "$price"}}},
    {'$sort': {"totalRevenue": -1}}
]

result = list(db.products.aggregate(pipeline))

# Iterate through the results and print formatted output
print("Product Categories by Total Revenue:")
for category in result:
    print(f"Category: {category['_id']}, Total Revenue: ${category['totalRevenue']:.2f}")

