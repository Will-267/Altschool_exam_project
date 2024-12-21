from database_connection import db
from pymongo import MongoClient
from datetime import datetime



# Function to convert string dates to ISODate
def convert_dates_to_iso():
    for order in db.orders.find():
        update_fields = {}
        if isinstance(order.get("order_date"), str):
            update_fields["order_date"] = datetime.strptime(order["order_date"], "%Y-%m-%dT%H:%M:%SZ")
        if isinstance(order.get("delivery_date"), str):
            update_fields["delivery_date"] = datetime.strptime(order["delivery_date"], "%Y-%m-%dT%H:%M:%SZ")
        if update_fields:  # Only update if there are fields to update
            db.orders.update_one({"_id": order["_id"]}, {"$set": update_fields})

# Call the conversion function
convert_dates_to_iso()

