import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")

# Sort events by patient and recorded event order
df["event_order_num"] = pd.to_numeric(
    df["event_order"],
    errors="coerce"
)

df_sorted = df.sort_values(
    ["case_id", "event_order_num"]
).copy()

# Get the previous event timestamp for each patient
df_sorted["previous_timestamp"] = (
    df_sorted.groupby("case_id")["timestamp"]
    .shift(1)
)

# Find timestamps that move backward
backward_timestamps = df_sorted[
    df_sorted["timestamp"]
    < df_sorted["previous_timestamp"]
]

print("Backward timestamp sequences:")
print(backward_timestamps[
    [
        "case_id",
        "event_order",
        "activity",
        "previous_timestamp",
        "timestamp"
    ]
])

print(
    "\nNumber of backward timestamp sequences:",
    len(backward_timestamps)
)

# Sort records by patient and event order
df_sorted = df.sort_values(
    ["case_id", "event_order"]
).copy()

# Get the previous activity for each patient
df_sorted["previous_activity"] = (
    df_sorted.groupby("case_id")["activity"].shift(1)
)

# Find consecutive repeated activities
repeated_activities = df_sorted[
    df_sorted["activity"]
    == df_sorted["previous_activity"]
]

print("Repeated consecutive activities:")
print(
    repeated_activities[
        [
            "case_id",
            "event_order",
            "previous_activity",
            "activity",
            "timestamp"
        ]
    ]
)

print(
    "\nNumber of repeated consecutive activities:",
    len(repeated_activities)
)

# Sort events chronologically within each patient case
df["timestamp"]=pd.to_datetime(df["timestamp"],errors="coerce")
df= df.sort_values(
    ["case_id", "timestamp", "event_order"]
).copy()

# Get the next activity and its timestamp
df["next_activity"] = (
    df.groupby("case_id")["activity"].shift(-1)
)

df["next_timestamp"] = (
    df.groupby("case_id")["timestamp"].shift(-1)
)

# Calculate the time difference in minutes
df["transition_minutes"] = (
    df["next_timestamp"]
    - df["timestamp"]
).dt.total_seconds() / 60

# Display patient transition details
print(
    df[
        [
            "case_id",
            "activity",
            "timestamp",
            "next_activity",
            "next_timestamp",
            "transition_minutes"
        ]
    ].head(20)
)

# Check negative transition times
negative_times = df_sorted[
    df["transition_minutes"] < 0
]

print("\nNegative transition times:", len(negative_times))

# Check unusually long gaps exceeding 180 minutes
long_gaps = df[
    df["transition_minutes"] > 180
]

print("\nTransitions exceeding 180 minutes:")
print(long_gaps[
    [
        "case_id",
        "activity",
        "next_activity",
        "transition_minutes"
    ]
])
# Count AFFECTED PATIENT CASES
print("\n Number of unique cases requiring reviews:",long_gaps["case_id"].nunique())


 data-quality summary

summary = {
    "Total records": len(df),

    "Unique patient cases": df["case_id"].nunique(),

    "Total missing values": df.isnull().sum().sum(),

    "Exact duplicate rows": df.duplicated().sum(),

    "Invalid timestamps": df["timestamp"].isna().sum(),

    "Backward timestamp sequences": len(backward_timestamps),

    "Negative transition times": len(negative_times),

    "Transitions over 180 minutes": len(long_gaps),

    "Repeated consecutive activities": len(repeated_activities)
}

print("CAREFLOW DATA QUALITY REPORT")
print("-" * 40)

for check, result in summary.items():
    print(f"{check}: {result}")



    summary_df = pd.DataFrame(
    list(summary.items()),
    columns=["Data Quality Check", "Result"]
)

summary_df.to_csv(
    "careflow_data_quality_summary.csv",
    index=False
)

print("Data-quality summary saved successfully.")
