# CareFlow — Day 3: dbt Model Design

## 1. Objective

The objective of Day 3 is to prepare the initial dbt staging model design and define the basic data-quality checks for CareFlow.

## 2. Source Dataset

Dataset: careflow_synthetic_500_patients.csv

The dataset contains synthetic hospital event records for 500 patients.

Important columns:
- case_id
- event_id
- event_order
- activity
- timestamp
- department
- journey_type
- is_loop_back
- data_source

## 3. Staging Model

Planned model name: stg_careflow_events

Purpose:
- Read data from the raw BigQuery event table.
- Standardize column names.
- Convert fields to appropriate data types where required.
- Preserve patient journey and event sequence information.
- Prepare clean data for later process-mining analysis.

## 4. Planned Transformations

- Keep the nine required event-log columns.
- Standardize column names consistently.
- Convert timestamp to a valid timestamp data type.
- Check event_order for each patient journey.
- Preserve loop-back information.
- Avoid removing records without a documented reason.

## 5. Planned Data-Quality Tests

- case_id should not be null.
- event_id should not be null.
- event_id should be unique if the source data design confirms uniqueness.
- timestamp should be valid.
- is_loop_back should contain valid Boolean values.
- event_order should be checked for valid sequencing within each patient journey.

## 6. Dependencies

Before running the model, the following are required:

- BigQuery raw table loaded by Gouri.
- Confirmed Google Cloud project ID.
- Confirmed BigQuery dataset and table names.
- Authorized dbt connection.
- dbt project configuration.

## 7. Current Status

Day 3: Model design and transformation requirements documented.

Pending:
- BigQuery source configuration.
- dbt project setup and connection.
- SQL model execution.
- Automated test execution.

No successful execution is claimed until the model and tests have been run and verified.
