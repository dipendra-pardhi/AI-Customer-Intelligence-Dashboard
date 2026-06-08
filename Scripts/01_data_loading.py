import pandas as pd
from sqlalchemy import create_engine

# Database Connection
DB_USER = "postgres"
DB_PASSWORD = "1165807946"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "olist_ecommerce_db"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Database Connected Successfully!")

# Load CSV Files
customers = pd.read_csv("Data/olist_customers_dataset.csv")
orders = pd.read_csv("Data/olist_orders_dataset.csv")
order_items = pd.read_csv("Data/olist_order_items_dataset.csv")
payments = pd.read_csv("Data/olist_order_payments_dataset.csv")
reviews = pd.read_csv("Data/olist_order_reviews_dataset.csv")
products = pd.read_csv("Data/olist_products_dataset.csv")
sellers = pd.read_csv("Data/olist_sellers_dataset.csv")

# Upload to PostgreSQL
customers.to_sql("customers", engine, if_exists="replace", index=False)
orders.to_sql("orders", engine, if_exists="replace", index=False)
order_items.to_sql("order_items", engine, if_exists="replace", index=False)
payments.to_sql("payments", engine, if_exists="replace", index=False)
reviews.to_sql("reviews", engine, if_exists="replace", index=False)
products.to_sql("products", engine, if_exists="replace", index=False)
sellers.to_sql("sellers", engine, if_exists="replace", index=False)

print("All Tables Loaded Successfully!")

print("Loading customers...")
customers = pd.read_csv("Data/olist_customers_dataset.csv")

print("Loading orders...")
orders = pd.read_csv("Data/olist_orders_dataset.csv")

print("Loading order_items...")
order_items = pd.read_csv("Data/olist_order_items_dataset.csv")

print("Loading payments...")
payments = pd.read_csv("Data/olist_order_payments_dataset.csv")

print("Loading reviews...")
reviews = pd.read_csv("Data/olist_order_reviews_dataset.csv")

print("Loading products...")
products = pd.read_csv("Data/olist_products_dataset.csv")

print("Loading sellers...")
sellers = pd.read_csv("Data/olist_sellers_dataset.csv")

print("CSV Loading Completed!")
