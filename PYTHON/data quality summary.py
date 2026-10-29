# Day 1 data-quality summary

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
