## Dataset Review

The CareFlow dataset contains synthetic hospital patient event data.

- Dataset file: careflow_synthetic_500_patients.csv
- Unique patients: 500
- Event records: 3,351
- Total columns: 9
- Missing values detected: 0
- Exact duplicate rows detected: 0

These results are based on the initial local CSV review. BigQuery and dbt validation are still pending.

## Important Event Columns

- case_id: Identifies each patient's journey.
- event_id: Identifies an individual event.
- event_order: Defines the event sequence.
- activity: Records the activity performed.
- timestamp: Records when an event occurred.
- department: Identifies the hospital department.
- journey_type: Describes the type of patient journey.
- is_loop_back: Indicates whether an event is a loop-back.
- data_source: Identifies the source of the data.

## Day 1 Tasks

1. Understand the purpose of dbt.
2. Review the CareFlow CSV structure.
3. Understand the BigQuery connection requirements.
4. Document the initial data-quality checks.
5. Prepare for the initial dbt staging model.

## Planned Next Steps

1. Confirm that the raw event table is available in BigQuery.
2. Obtain the correct BigQuery project, dataset, and table details.
3. Configure dbt for BigQuery.
4. Create an initial staging model using SQL.
5. Add basic data-quality tests.
6. Compare the transformed data with the raw event data.

## Current Status

Day 1: Initial documentation and dataset review.

Pending: BigQuery connection, dbt project setup, staging model, and test execution.

These tasks will be marked complete after verification.


