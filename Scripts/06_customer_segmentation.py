import pandas as pd
from sklearn.cluster import KMeans

print("Loading Customer Features...")

# Load Feature Dataset
df = pd.read_csv("Data/Processed/customer_features.csv")

print("Dataset Shape:", df.shape)

# K-Means ke liye sirf total_orders use karenge
X = df[["total_orders"]]

# KMeans Model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df["cluster"] = kmeans.fit_predict(X)

# Cluster Summary
print("\nCustomer Segments:")
print(df["cluster"].value_counts())

# Save Output
df.to_csv(
    "Data/Processed/customer_segments.csv",
    index=False
)

print("\nCustomer Segmentation Completed!")