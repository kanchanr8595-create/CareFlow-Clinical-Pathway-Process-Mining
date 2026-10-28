# CareFlow — Patient Transition-Time Analysis

**Task:** Week 3 — Day 2  
**Tool:** Google BigQuery

## Objective
Analyze the time taken for patients to move between consecutive clinical activities and identify transitions that may require further investigation.

## Work Completed
A BigQuery SQL query was executed using the `LEAD()` window function to identify the next activity and its timestamp for each patient case. The query calculates the number of occurrences for each activity transition and the average transition time in minutes using `TIMESTAMP_DIFF()`. Results are sorted by average transition time in descending order.

## Results
**Query Status:** Successfully executed.

The output includes the current activity, next activity, transition count, and average transition time in minutes. These results can help identify transitions with longer average durations for further investigation. Specific metrics and bottleneck findings should be added after reviewing the actual query output.

## Next Steps
Review the results, validate data quality, and investigate longer-duration transitions to determine whether they indicate potential bottlenecks.
