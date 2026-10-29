# CareFlow Bottleneck Analysis

## Objective
Identify activity transitions with higher average transition times using the CareFlow process-mining dataset in BigQuery.

## Method
Used SQL window functions to identify the next activity and timestamp for each case. Transition counts and average transition times in minutes were calculated for each activity pair.

## Key Findings
- **Imaging → Treatment:** Highest average transition time of 96.09 minutes across 96 transitions.
- **Doctor Consultation → Treatment:** Average of 90.04 minutes across 91 transitions.
- **Lab Test → Treatment:** Average of 88.22 minutes across 313 transitions.
- **Triage → Doctor Consultation:** Highest transition count, with 500 transitions averaging 82.29 minutes.
- **Registration → Triage:** Lowest average transition time of 20.06 minutes across 500 transitions.

## Interpretation
Transitions with higher average durations are candidates for further investigation. The high frequency of Triage → Doctor Consultation also makes it an important pathway to examine.

## Limitations
The results show observed transition times but do not establish the causes of delays or their clinical impact. Further validation is required before confirming bottlenecks.

## Evidence
The transition-time query results were exported to CSV and used for this analysis.
