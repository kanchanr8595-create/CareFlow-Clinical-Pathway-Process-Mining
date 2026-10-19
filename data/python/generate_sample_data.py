
from pathlib import Path
from generate_careflow_data import generate_event_log

# Generate a separate sample for 20 patients
sample = generate_event_log(20)

# Save it separately so the original 500-patient CSV stays safe
output_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "careflow_sample_20_patients.csv"
)

sample.to_csv(output_path, index=False)

print("Sample dataset created successfully.")
print("Unique patients:", sample["case_id"].nunique())
print("Total events:", len(sample))
print("Columns:", list(sample.columns))
print("Output file:", output_path)
