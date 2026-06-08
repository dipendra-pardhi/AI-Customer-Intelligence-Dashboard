import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1165807946@localhost:5432/olist_ecommerce_db"
)

print("Loading Orders Data...")

orders = pd.read_sql(
    "SELECT * FROM orders",
    engine
)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

monthly_orders = (
    orders.groupby(
        orders["order_purchase_timestamp"].dt.to_period("M")
    )
    .size()
    .reset_index(name="orders")
)

monthly_orders["month"] = (
    monthly_orders["order_purchase_timestamp"]
    .astype(str)
)

# Remove incomplete months
monthly_orders = monthly_orders[
    monthly_orders["orders"] > 100
]

print("\nMonthly Orders Preview:")
print(monthly_orders.tail())

monthly_orders.to_csv(
    "Data/Processed/monthly_orders.csv",
    index=False
)

print("\nMonthly Orders Dataset Created Successfully!")