import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

print("Timestamp data type:", df["timestamp"].dtype)

print(
    "Invalid timestamps:",
    df["timestamp"].isnull().sum()
)

print("Earliest timestamp:", df["timestamp"].min())
print("Latest timestamp:", df["timestamp"].max())

print(df[["case_id", "activity", "timestamp"]].head())
