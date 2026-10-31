## Dataset and method
- Source file: `careflow_synthetic_500_patients.csv`
- Cases: **500**
- Events: **3,351**
- Consecutive transitions calculated: **2,851**
- Events were ordered within each case by parsed timestamp, with `event_order` as a tie-breaker.
- Transition time = next event timestamp minus current event timestamp, in minutes.

## Overall results
- Negative transition times: **0**
- Zero-minute transitions: **0**
- Minimum transition: **5 minutes**
- Median transition: **46 minutes**
- Average transition: **55.65 minutes**
- Maximum transition: **240 minutes**
- Transitions longer than 180 minutes: **87**

**Interpretation:** No negative or zero transitions were found. There are 87 transitions longer than 180 minutes; these are candidates for review, not proof of a clinical bottleneck. Confirm them against journey context and the team's agreed threshold.

## Results by activity pair

| Current activity | Next activity | Transition count | Average minutes | Median minutes | Maximum minutes |
|---|---|---:|---:|---:|---:|
| Imaging | Treatment | 96 | 96.09 | 90.00 | 240 |
| Doctor Consultation | Treatment | 91 | 90.04 | 78.00 | 235 |
| Lab Test | Treatment | 313 | 88.22 | 80.00 | 240 |
| Triage | Doctor Consultation | 500 | 82.29 | 70.00 | 240 |
| Lab Test | Doctor Consultation | 48 | 65.17 | 68.50 | 100 |
| Lab Test | Imaging | 127 | 53.78 | 56.00 | 90 |
| Doctor Consultation | Lab Test | 488 | 49.58 | 49.00 | 90 |
| Imaging | Doctor Consultation | 61 | 48.89 | 45.00 | 95 |
| Treatment | Discharge | 500 | 44.30 | 45.00 | 75 |
| Doctor Consultation | Imaging | 30 | 40.20 | 30.00 | 89 |
| Discharge | Follow-up | 97 | 20.09 | 20.00 | 35 |
| Registration | Triage | 500 | 20.06 | 20.00 | 35 |

## Transitions over 180 minutes
- `Triage → Doctor Consultation`: 45 transitions over 180 minutes
- `Lab Test → Treatment`: 23 transitions over 180 minutes
- `Doctor Consultation → Treatment`: 10 transitions over 180 minutes
- `Imaging → Treatment`: 9 transitions over 180 minutes

These longer gaps are concentrated in the activity pairs above. Investigate the relevant case records and confirm whether the gaps are expected in the synthetic journey design before reporting causes.

## BigQuery SQL template

Replace `project_id.dataset_id.table_name` with the team's actual BigQuery table. The CSV uses lowercase column names (`case_id`, `activity`, `timestamp`), so this template follows that schema. `SAFE_CAST` handles the possibility that `timestamp` is stored as a string; rows that fail parsing should be checked separately.

## Conclusion
The local CSV analysis produced 2,851 transitions. The observed average is 55.65 minutes, median is 46 minutes, and maximum is 240 minutes. There are no negative or zero transitions. 87 transitions exceed 180 minutes and should be reviewed in context.
