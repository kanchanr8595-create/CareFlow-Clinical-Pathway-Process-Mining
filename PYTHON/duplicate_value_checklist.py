import numpy as np
import pandas as pd



df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")

# Display the first five rows
print(df.head())

# Check rows and columns
print("Dataset shape:", df.shape)

# Display column names
print(df.columns.tolist())

# Check complete duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# Display duplicate rows
print(df[df.duplicated()])

# Check duplicate event IDs
print("Duplicate event IDs:", df["event_id"].duplicated().sum())

# Check duplicate case ID and event order combinations
print(
    "Duplicate case-order combinations:",
    df.duplicated(subset=["case_id", "event_order"]).sum()
)
