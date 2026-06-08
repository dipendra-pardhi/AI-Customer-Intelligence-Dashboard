import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1165807946@localhost:5432/olist_ecommerce_db"
)

orders = pd.read_sql("SELECT * FROM orders", engine)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

monthly_orders = (
    orders.groupby(
        orders["order_purchase_timestamp"].dt.to_period("M")
    )
    .size()
)

monthly_orders.plot(figsize=(12,6))
plt.title("Monthly Orders Trend")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.grid(True)

plt.show()