import numpy as np
import pandas as pd



df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")

print(df.head())

print("Dataset shape:", df.shape)

print(df.columns.tolist())

print("Duplicate rows:", df.duplicated().sum())

print(df[df.duplicated()])

print("Duplicate event IDs:", df["event_id"].duplicated().sum())

print(
    "Duplicate case-order combinations:",
    df.duplicated(subset=["case_id", "event_order"]).sum()
)
