
import pandas as pd
from pathlib import Path

# Locate the CSV in the repository
csv_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "careflow_synthetic_500_patients.csv"
)

df = pd.read_csv(csv_path)

required_columns = [
    "case_id",
    "event_id",
    "event_order",
    "activity",
    "timestamp",
    "department",
    "journey_type",
    "is_loop_back",
    "data_source",
]

print("CAREFLOW DATA VALIDATION")
print("-" * 30)

# 1. Check required columns
missing_columns = [
    col for col in required_columns if col not in df.columns
]
print("Missing required columns:", missing_columns)

# 2. Count unique patients
print("Total event rows:", len(df))
print("Unique patients:", df["case_id"].nunique())

# 3. Check missing values
print("\nMissing values by column:")
print(df[required_columns].isnull().sum())

# 4. Check duplicate event IDs
print("\nDuplicate event IDs:", df["event_id"].duplicated().sum())

# 5. Check invalid timestamps
timestamps = pd.to_datetime(df["timestamp"], errors="coerce")
print("Invalid timestamps:", timestamps.isna().sum())

# 6. Check duplicate patient-event order pairs
print(
    "Duplicate patient/event-order pairs:",
    df.duplicated(subset=["case_id", "event_order"]).sum()
)

# 7. Check chronological order within each patient
check_df = df.assign(parsed_timestamp=timestamps)
out_of_order = 0

for _, group in check_df.groupby("case_id"):
    ordered = group.sort_values("event_order")["parsed_timestamp"]
    out_of_order += int((ordered.diff().dropna().dt.total_seconds() < 0).sum())

print("Events out of chronological order:", out_of_order)
print("\nValidation checks completed.")
