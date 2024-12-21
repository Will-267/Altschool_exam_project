import os
import json
from database_connection import db

# Map collection names to MongoDB collections
collections_map= {
    "customers.json": db["customers"],
    "products.json": db["products"],
    "orders.json": db["orders"],
    "order_items.json": db["order_items"],
}

#file_path = "C:\Users\USER\Desktop\my_alschool_project\data"

def load_data_from_file(file_path, collection):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file) #Load JSON data
            collection.insert_many(data) #Insert data into MongoDB
            print(f"Successfully loaded data from {file_path} into {collection.name} collection,")
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        
def load_all_data(data_folder):
    
    for filename in os.listdir(data_folder):
        if filename in collections_map:
            file_path = os.path.join(data_folder, filename)
            collection = collections_map[filename]
            load_data_from_file(file_path, collection)
if __name__ == "__main__":
    data_folder = r"C:\Users\USER\Desktop\my_alschool_project\data"
    load_all_data(data_folder)