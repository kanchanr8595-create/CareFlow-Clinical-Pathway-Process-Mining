# CareFlow — Day 7 Staging Model Plan

## 1. Objective

The objective of Day 7 is to define the first dbt staging model for the CareFlow synthetic hospital event-log dataset.

## 2. Source Data

The source dataset contains synthetic patient journey events.

The expected columns are:

- `case_id`
- `event_id`
- `event_order`
- `activity`
- `timestamp`
- `department`
- `journey_type`
- `is_loop_back`
- `data_source`

The final column names and data types must be verified against the actual BigQuery raw table before implementation.

## 3. Proposed Staging Model

Model name: `stg_careflow_events`

Purpose:

- Prepare raw event-log data for downstream analysis.
- Keep the fields required to reconstruct patient journeys.
- Make timestamps and event-order fields suitable for analysis.
- Preserve loop-back and journey-type information for process mining.

## 4. Planned Transformations

1. Select the required source columns.
2. Apply suitable data types after checking the source schema.
3. Check for null patient and event identifiers.
4. Validate timestamp values.
5. Review event ordering within each patient journey.
6. Preserve the original event rows unless a documented transformation requires otherwise.

## 5. Planned Validation

The staging model will be validated by:

- Comparing raw and staging row counts.
- Checking required fields for null values.
- Checking event ID uniqueness if the source design requires unique event IDs.
- Checking timestamp and event-order validity.
- Reviewing unexpected changes in journey information.

## 6. Dependencies

Implementation requires:

- A confirmed BigQuery raw table.
- BigQuery project, dataset, and table names.
- A configured dbt development environment.
- Appropriate access and authentication.

## 7. Current Status

This document describes the planned staging model. The SQL model has not been confirmed as implemented or executed.

The next step is to verify the source schema and dbt project configuration before writing and running the model.

## 8. Day 7 Outcome

The initial staging model design and its validation requirements are documented for the CareFlow project.
