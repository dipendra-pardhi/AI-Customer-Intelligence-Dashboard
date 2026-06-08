import pandas as pd
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:1165807946@localhost:5432/olist_ecommerce_db"
)

# Load Tables
customers = pd.read_sql("SELECT * FROM customers", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)
products = pd.read_sql("SELECT * FROM products", engine)

print("\n===== DATA QUALITY REPORT =====")

print("\nCustomers Shape:", customers.shape)
print("Orders Shape:", orders.shape)
print("Products Shape:", products.shape)

print("\nMissing Values:")
print(customers.isnull().sum())

print("\nDuplicate Rows:")
print("Customers:", customers.duplicated().sum())
print("Orders:", orders.duplicated().sum())
print("Products:", products.duplicated().sum())