import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("Loading Feature Dataset...")

df = pd.read_csv("customer_features.csv")

print("Dataset Shape:", df.shape)

# Dummy Target Variable
df["target"] = (df["total_orders"] > 1).astype(int)

X = df[["total_orders"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nMachine Learning Model Completed!")