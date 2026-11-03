
# Week 3 - Transition Time Analysis

## 1. Objective
To verify patient event ordering and calculate the time between consecutive hospital activities.

## 2. Dataset Details
- Dataset: CareFlow Synthetic Patient Event Log
- Patients: 500
- Total events: 3351
- Data type: Synthetic data

## 3. Python Analysis
- Events were sorted patient-wise by timestamp.
- The next activity was identified using Pandas.
- Time differences were calculated in minutes.
- Average, median and maximum transition times were calculated.

## 4. Validation Results
- Missing values: 0
- Duplicate event IDs: 0
- Invalid timestamps: 0
- Out-of-order events: 0

## 5. Transition Analysis
Refer to careflow_transition_time_analysis.xlsx for the actual transition summary and patient-level details.

## 6. Findings
The transition results will be reviewed to identify activity pairs requiring further bottleneck investigation.

## 7. Pending Work
- Cross-check Python results with BigQuery results.
- Review unusual transition times.
- Compare findings with the PM4Py process map.

## 8. Conclusion
Python-based patient transition analysis has been prepared using the synthetic CareFlow event log.
