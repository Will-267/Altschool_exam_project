from database_connection import db

# Aggregation pipeline to calculate average delivery time
pipeline = [
    {
        "$project": {  
            "delivery_time_days": {
                "$divide": [
                    { "$subtract": ["$delivery_date", "$order_date"] },
                    1000 * 60 * 60 * 24  
                ]
            }
        }
    },
    {
        "$group": {  
            "_id": None,
            "average_delivery_time": { "$avg": "$delivery_time_days" }
        }
    },
    {
        "$project": {  
            "_id": 0,
            "average_delivery_time": 1
        }
    }
]

# Execute the pipeline
result = list(db.orders.aggregate(pipeline))

# Display the result
if result:
    print(f"Average Delivery Time (in days): {result[0]['average_delivery_time']:.2f}")
else:
    print("No data found.")