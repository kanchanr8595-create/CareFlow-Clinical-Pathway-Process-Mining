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
