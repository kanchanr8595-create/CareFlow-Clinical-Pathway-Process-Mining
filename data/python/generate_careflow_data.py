"""
CareFlow synthetic event-log generator.
Creates a reproducible, synthetic clinical pathway event log for 500 patients.
No real patient data is used.
Run: python generate_careflow_data.py
"""
import random
from datetime import datetime, timedelta
import pandas as pd

random.seed(42)

def generate_event_log(patient_count=500):
    rows = []
    start_date = datetime(2026, 9, 1, 8, 0, 0)
    departments = {
        "Registration": "Reception",
        "Triage": "Emergency",
        "Doctor Consultation": "Emergency",
        "Lab Test": "Laboratory",
        "Imaging": "Radiology",
        "Treatment": "Emergency",
        "Discharge": "Reception",
        "Follow-up": "Outpatient",
    }

    for i in range(1, patient_count + 1):
        case_id = f"P{i:04d}"
        current_time = start_date + timedelta(
            days=random.randint(0, 13),
            minutes=random.randint(0, 600)
        )
        journey_type = random.choices(
            ["normal", "delayed", "loop_back", "complex"],
            weights=[0.55, 0.20, 0.15, 0.10],
            k=1
        )[0]

        journey = ["Registration", "Triage", "Doctor Consultation"]
        if journey_type in ("loop_back", "complex") or random.random() < 0.72:
            journey.append("Lab Test")
        if journey_type == "complex" or random.random() < 0.25:
            journey.append("Imaging")
        if journey_type == "loop_back":
            journey.extend(["Doctor Consultation", "Lab Test"])
        elif journey_type == "complex":
            journey.extend(["Doctor Consultation", "Lab Test"])
        journey.extend(["Treatment", "Discharge"])
        if random.random() < 0.20:
            journey.append("Follow-up")

        for seq, activity in enumerate(journey, start=1):
            if seq > 1:
                if journey_type == "delayed" and activity in ("Doctor Consultation", "Treatment"):
                    wait = random.randint(90, 240)
                elif activity == "Doctor Consultation":
                    wait = random.randint(15, 100)
                elif activity in ("Lab Test", "Imaging"):
                    wait = random.randint(10, 90)
                elif activity == "Treatment":
                    wait = random.randint(20, 120)
                elif activity == "Discharge":
                    wait = random.randint(15, 75)
                else:
                    wait = random.randint(5, 35)
                current_time += timedelta(minutes=wait)

            rows.append({
                "case_id": case_id,
                "event_id": f"{case_id}-E{seq:02d}",
                "event_order": seq,
                "activity": activity,
                "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "department": departments[activity],
                "journey_type": journey_type,
               "is_loop_back": (
    activity == "Doctor Consultation"
    and journey[:seq].count("Doctor Consultation") > 1
),
                "data_source": "synthetic",
            })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    event_log = generate_event_log(500)
    event_log.to_csv("careflow_synthetic_500_patients.csv", index=False)
    print(f"Generated {event_log['case_id'].nunique()} patients and {len(event_log)} events.")
