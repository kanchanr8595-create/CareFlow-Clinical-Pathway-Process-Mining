# CareFlow – Bottleneck Analysis

## Objective

To identify patient activity transitions with higher average transition times and understand where further investigation may be required.

## Work Completed

- Executed SQL queries using `LEAD()`, `TIMESTAMP_DIFF()`, `COUNT()`, and `AVG()`.
- Calculated transition counts between consecutive activities.
- Calculated average transition times in minutes.
- Sorted the results by average transition time in descending order.

## Key Findings

| Activity Transition | Average Transition Time | Transition Count |
|---|---:|---:|
| Imaging → Treatment | 96.09 minutes | 96 |
| Doctor Consultation → Treatment | 90.04 minutes | 91 |
| Lab Test → Treatment | 88.22 minutes | 313 |
| Triage → Doctor Consultation | 82.29 minutes | 500 |

## Observation

Imaging → Treatment has the highest average transition time, while Triage → Doctor Consultation has the highest transition count.

These transitions are potential areas for further investigation. However, the results alone do not establish the causes of delays.

## Outcome

The transition-time analysis was completed, and the results were recorded for further process-mining analysis.
