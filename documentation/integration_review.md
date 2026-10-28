# Week 3 Day 1 — CareFlow Integration Review

## 1. Objective
Review the dbt staging model and prepare CareFlow event data for integration with the clinical pathway process-mining workflow.

## 2. Data Source
- Google Cloud project: `care-flow-clinical-pathway`
- BigQuery dataset: `careflow_dataset`
- dbt source: `careflow.raw_events`
- Expected source records: 3,351
- Exact BigQuery table name: Pending verification.

## 3. dbt Staging Transformation
Model: `stg_careflow_events.sql`

The staging model:
- Trims whitespace from text fields.
- Converts `case_id` and `event_id` to strings.
- Converts `event_order` to an integer.
- Converts `timestamp` to a BigQuery TIMESTAMP as `event_timestamp`.
- Converts `is_loop_back` to a Boolean.
- Converts blank text values to NULL.

## 4. Integration Fields

| Output field | Source field |
|---|---|
| Case_ID | case_id |
| Activity_Name | activity |
| Timestamp | event_timestamp |

These fields support the downstream clinical pathway event sequence. Final output naming should be aligned with the team's agreed schema.

## 5. Validation Status
- Source configuration reviewed.
- Staging SQL reviewed.
- BigQuery source table name: Not yet verified.
- dbt execution status: Requires confirmation from the latest run.
- dbt test status: Requires confirmation from the latest test output.
- Record count and output schema: Pending validation against BigQuery.

## 6. Dependencies and Next Actions
1. Confirm the exact raw BigQuery table name.
2. Run the staging model using dbt.
3. Run the configured dbt tests.
4. Verify the output record count and required fields.
5. Coordinate the final field names with the clinical pathway integration team.

## 7. Day 1 Outcome
The staging transformation and integration requirements have been reviewed. Successful execution and data validation will be recorded after the corresponding checks are confirmed.
