# CareFlow — Day 6 dbt Implementation Readiness Review

## 1. Objective

The objective of Day 6 is to check whether the required resources are ready for the initial dbt implementation in the CareFlow project.

## 2. Required Prerequisites

Before running dbt, the following items must be confirmed:

- [ ] The synthetic CareFlow CSV file is available.
- [ ] The raw event-log table has been created in BigQuery.
- [ ] The BigQuery project ID and dataset name are confirmed.
- [ ] The raw table name and column names are verified.
- [ ] Access to the required BigQuery resources is available.
- [ ] A development environment for dbt is available.
- [ ] BigQuery connection and authentication are configured securely.

## 3. Planned Staging Model

The first staging model will be named:

`stg_careflow_events`

Its purpose will be to prepare the raw CareFlow event log for further analysis.

Planned activities:

- Select the required event-log columns.
- Standardize column names and data types where required.
- Check patient IDs and event IDs.
- Validate event timestamps and event order.
- Preserve the original event information needed for process mining.

## 4. Planned Data Tests

The initial tests will check:

- `case_id` is not null.
- `event_id` is not null.
- Each `event_id` is unique, if the dataset design confirms it should be unique.
- `timestamp` is valid.
- `event_order` is valid for each patient journey.
- The transformed row count can be compared with the raw table.

## 5. Current Status

The staging model and tests are planned but have not been confirmed as executed.

The actual implementation depends on BigQuery table availability and a working dbt development environment.

No successful BigQuery connection, model execution, or test result should be reported until it has been verified.

## 6. Next Steps

1. Confirm the raw table status with the BigQuery workstream.
2. Confirm the BigQuery project, dataset, and table names.
3. Set up the dbt development environment.
4. Create the initial staging model.
5. Run the model and tests when access is available.
6. Record the actual results and any errors.

## 7. Day 6 Outcome

The prerequisites and pending dependencies for dbt implementation are documented. Actual execution will be completed when the required resources are ready.
