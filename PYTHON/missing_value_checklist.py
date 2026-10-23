import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")
# Count missing values in each column
print(df.isnull().sum())

# Count all missing cells
print("Total missing values:", df.isnull().sum().sum())

# Display rows containing any missing values
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)

# Calculate percentage of missing values
print((df.isnull().sum() / len(df) * 100).round(2))
