# Event Data Verification

## Objective
Verify that the CareFlow event-log data is correctly accessible in BigQuery and that the key fields required for process mining are available.

## Validation Performed
Retrieved sample event records using SQL and checked the `case_id`, `activity`, `timestamp`, and `event_order` fields. The records were sorted by case ID and event order to review the chronological sequence of activities.

## Result
The query executed successfully and returned 10 sample records for verification.

## Status
Sample event data verification completed.
