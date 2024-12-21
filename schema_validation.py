def apply_products_validation(db):
    try:
        if "product" not in db.list_collection_names():
            db.create_collection(
                "product",
                validator = {
                    "jsonSchema": {
                        "bsonType": "object",
                        "required":  ["product_id", "product_name", "category", "price"],
                        "properties": {
                            "product_id": {"bsonType": "int", "description": "Must be an integer"},
                            "product_name": {"bsonType": "string", "description": "Must be a string"},
                            "category": {"bsonType": "string", "description": "Must be a string"},
                            "price": {
                                "bsonType": "double",
                                "minimum": 0,
                                "description": "Must be a number greater or equal to 0"
                            }
                        }
                    }
                    }# Add json schema here
            )
        else:
            db.command(
                "collMod",
                "product",
                validator = {"jsonSchema": {
                        "bsonType": "object",
                        "required":  ["product_id", "product_name", "category", "price"],
                        "properties": {
                            "product_id": {"bsonType": "int", "description": "Must be an integer"},
                            "product_name": {"bsonType": "string", "description": "Must be a string"},
                            "category": {"bsonType": "string", "description": "Must be a string"},
                            "price": {
                                "bsonType": "double",
                                "minimum": 0,
                                "description": "Must be a number greater or equal to 0"
                            }
                        }
                    }
                    }} # add json schema here
            validationLevel = "strict",
            validationAction = "error"
            )
    except Exception as e:
        print(f"Error applying validation: {e}")