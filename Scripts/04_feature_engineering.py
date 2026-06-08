import pandas as pd
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:1165807946@localhost:5432/olist_ecommerce_db"
)

print("Loading Data...")

customers = pd.read_sql("SELECT * FROM customers", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)

# Date Conversion
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Customer Order Count
customer_orders = (
    orders.groupby("customer_id")
    .size()
    .reset_index(name="total_orders")
)

# Merge Features
features = customers.merge(
    customer_orders,
    on="customer_id",
    how="left"
)

features["total_orders"] = features["total_orders"].fillna(0)

print("\nFeature Dataset Shape:")
print(features.shape)

print("\nTop 10 Records:")
print(features.head(10))

# Save
features.to_csv(
    "customer_features.csv",
    index=False
)

print("\nFeature Engineering Completed!")