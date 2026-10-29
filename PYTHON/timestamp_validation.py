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
