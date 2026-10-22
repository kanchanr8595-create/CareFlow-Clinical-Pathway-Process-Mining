# CareFlow — Day 2: dbt Staging Preparation

## 1. Objective

The objective of Day 2 is to prepare the initial dbt staging model and identify the data-quality checks required for CareFlow.

## 2. My Responsibility

I am responsible for dbt setup and initial transformation preparation.

## 3. Source Dataset

File: careflow_synthetic_500_patients.csv

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

## 4. Staging Model Purpose

The staging model will prepare the raw event data for further analysis.

Planned tasks:
- Standardize column names.
- Check data types.
- Convert timestamps to the appropriate timestamp data type.
- Preserve patient and event identifiers.
- Prepare the data for process-mining analysis.

## 5. Planned Data-Quality Tests

- case_id should not be null.
- event_id should not be null.
- event_id should be unique if each event is expected to have one unique identifier.
- timestamp should contain valid date and time values.
- event_order should be valid for each patient journey.
- is_loop_back should contain valid Boolean values.

## 6. Dependencies

The following items are still required before execution:
- BigQuery raw table availability.
- Google Cloud project ID.
- BigQuery dataset ID.
- Exact raw table name.
- Authorized dbt connection.

## 7. Day 2 Status

Completed when this plan is documented and reviewed.

The staging model has not yet been executed. BigQuery integration and automated tests remain pending.
