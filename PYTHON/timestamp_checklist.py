import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")
# Convert timestamp column into datetime
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

# Check the data type
print("Timestamp data type:", df["timestamp"].dtype)

# Check invalid timestamps
print(
    "Invalid timestamps:",
    df["timestamp"].isnull().sum()
)

# Display timestamp range
print("Earliest timestamp:", df["timestamp"].min())
print("Latest timestamp:", df["timestamp"].max())

# Display sample values
print(df[["case_id", "activity", "timestamp"]].head())
