import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1165807946@localhost:5432/olist_ecommerce_db"
)

print("Loading Data...")

query = """
SELECT
    c.customer_unique_id,

    COUNT(DISTINCT o.order_id) AS frequency,

    SUM(p.payment_value) AS monetary

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN payments p
ON o.order_id = p.order_id

GROUP BY c.customer_unique_id
"""

rfm = pd.read_sql(query, engine)

print(rfm.head())

rfm.to_csv(
    "Data/Processed/rfm_features.csv",
    index=False
)

print("RFM Features Created Successfully!")