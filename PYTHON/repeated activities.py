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
