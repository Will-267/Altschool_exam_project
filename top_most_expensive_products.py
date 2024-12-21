from database_connection import db
from pymongo import MongoClient

pipeline = [
    {
        "$lookup": {  
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product_details"
        }
    },
    {
        "$unwind": "$product_details"  
    },
    {
        "$group": {  
            "_id": "$order_id",
            "products": {
                "$push": {
                    "product_id": "$product_id",
                    "product_name": "$product_details.product_name",
                    "price": "$product_details.price"
                }
            }
        }
    },
    {
        "$project": {  
            "top_products": {
                "$slice": [
                    {
                        "$sortArray": {
                            "input": "$products",
                            "sortBy": { "price": -1 }
                        }
                    },
                    3
                ]
            }
        }
    }
]

# Execute the aggregation pipeline
result = list(db.order_items.aggregate(pipeline))

# Display results
print("Top 3 most expensive products sold in each order:")
for order in result:
    print(f"Order ID: {order['_id']}")
    for product in order["top_products"]:
        print(f"  Product Name: {product['product_name']}, Price: ${product['price']}")
        
