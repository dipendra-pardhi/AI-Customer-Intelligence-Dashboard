import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading RFM Features...")

df = pd.read_csv("Data/Processed/rfm_features.csv")

X = df[["frequency", "monetary"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)

print("\nCluster Distribution:")
print(df["cluster"].value_counts())

df.to_csv(
    "Data/Processed/customer_segments.csv",
    index=False
)

print("\nCustomer Segmentation Completed!")

cluster_map = {
    0: "💎 VIP Customers",
    1: "⚠️ At Risk Customers",
    2: "🛒 Regular Customers"
}

df["segment"] = df["cluster"].map(cluster_map)



import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading RFM Features...")

df = pd.read_csv("Data/Processed/rfm_features.csv")

X = df[["frequency", "monetary"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)

cluster_map = {
    0: "💎 VIP Customers",
    1: "⚠️ At Risk Customers",
    2: "🛒 Regular Customers"
}

df["segment"] = df["cluster"].map(cluster_map)

print("\nCluster Distribution:")
print(df["segment"].value_counts())

df.to_csv(
    "Data/Processed/customer_segments.csv",
    index=False
)

print("\nCustomer Segmentation Completed!")
