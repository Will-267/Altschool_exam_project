# E-Commerce Data Management System

This project is an E-commerce Data Management System built with Python and MongoDB. It includes features for managing customers, products, orders, and order items. It also incorporates advanced MongoDB operations such as aggregation pipelines. This project is designed to ensure data integrity and support efficient data processing for an e-commerce platform.

---

## **Features**

### **Core Functionality**

- **Customers Collection**: Stores customer details such as name, email, and address.
- **Products Collection**: Maintains product information including category, name, and price.
- **Orders Collection**: Tracks customer orders and delivery dates.
- **Order Items Collection**: Contains details of products in each order, including quantity and price.

### **Advanced Operations**

- **Aggregation Pipelines**: Implements queries to calculate metrics like average delivery time, highest revenue-generating categories, and top-selling products.

---

## **Project Structure**

```plaintext
.
├── database
│   ├── database_connection.py  # Handles MongoDB connection setup
├── data
│   ├── customers.json          # Dataset for customers collection
│   ├── products.json           # Dataset for products collection
│   ├── orders.json             # Dataset for orders collection
│   ├── order_items.json        # Dataset for order items collection
├── pipelines
│   ├── revenue_by_category.py  # Aggregation pipeline for revenue analysis
│   ├── average_delivery_time.py # Aggregation pipeline for delivery time calculation
│   ├── top_expensive_products.py # Aggregation pipeline for expensive products
├── main.py                     # Entry point for the project
├── README.md                   # Project documentation
```

---

## **Setup and Installation**

### **Prerequisites**

- Python 3.9 or higher
- MongoDB Community Edition

### **Installation Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-data-management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ecommerce-data-management
   ```

---

## **Usage**

### **Data Loading**

Data for each collection is stored in JSON files within the `data` folder. Run `main.py` to load the datasets into their respective collections.

### **Aggregation Pipelines**

Run any script in the `pipelines` folder to execute specific data analysis tasks. For example:

```bash
python pipelines/revenue_by_category.py
```

---

## **Examples**

### **Aggregation Pipeline: Calculate Average Delivery Time**

```python
pipeline = [
    {"$addFields": {"delivery_duration": {"$subtract": ["$delivery_date", "$order_date"]}}},
    {"$group": {"_id": None, "avgDeliveryTime": {"$avg": "$delivery_duration"}}}
]
result = list(db.orders.aggregate(pipeline))
print(result)
```

---


## **Acknowledgments**

- MongoDB documentation for providing comprehensive guides and examples.
- The Python community for tools and resources.

