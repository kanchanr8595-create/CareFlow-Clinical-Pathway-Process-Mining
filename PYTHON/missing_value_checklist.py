import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")
print(df.isnull().sum())

print("Total missing values:", df.isnull().sum().sum())

missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)

print((df.isnull().sum() / len(df) * 100).round(2))
