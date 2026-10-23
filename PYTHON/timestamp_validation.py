import numpy as np
import pandas as pd

df = pd.read_csv(r"/content/careflow_synthetic_500_patients.csv")


# Sort events by patient and event order
df = df.sort_values(["case_id", "event_order"])

# Compare each timestamp with the previous event
df["time_difference"] = (
    df.groupby("case_id")["timestamp"].diff()
)

# Find events where time moves backwards
backward_events = df[df["time_difference"] < pd.Timedelta(0)]

print("Backward timestamp sequences:", len(backward_events))
print(backward_events[
    ["case_id", "event_order", "activity",
     "timestamp", "time_difference"]
])


df = df.drop(columns=["time_difference"], errors="ignore")

df.to_csv("careflow_validated.csv", index=False)

print("Validated CSV saved successfully!")
