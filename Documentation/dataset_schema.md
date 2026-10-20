# CareFlow Dataset Schema

## 1. Purpose

This document describes the structure of the synthetic CareFlow patient event-log dataset. It explains the dataset columns and their use in BigQuery, SQL validation, and process-mining analysis.

## 2. Dataset Overview

- **Dataset file:** `careflow_synthetic_500_patients.csv`
- **Expected patients:** 500
- **Data type:** Synthetic clinical pathway event log
- **Main purpose:** To analyze patient journeys, waiting times, repeated activities, and potential hospital bottlenecks.
- **Privacy:** Synthetic data only; no real patient information is intended to be used.

## 3. Column Definitions

| Column | Description |
|---|---|
| `case_id` | Unique identifier for a patient journey |
| `event_id` | Unique identifier for an event |
| `event_order` | Sequence number of an event within a patient journey |
| `activity` | Clinical pathway activity, such as Registration, Triage, or Treatment |
| `timestamp` | Date and time when the activity occurs |
| `department` | Hospital department associated with the activity |
| `journey_type` | Type of journey: normal, delayed, loop_back, or complex |
| `is_loop_back` | Indicates whether a Doctor Consultation occurs more than once in the journey |
| `data_source` | Identifies records as synthetic |

## 4. Data Workflow

1. Python can generate synthetic patient event-log data.
2. BigQuery stores the raw event-log data for SQL analysis.
3. SQL validation checks data completeness, event identifiers, event order, and timestamps.
4. dbt can transform raw records into cleaned analytical models.
5. Process-mining analysis can investigate patient pathways, repeated activities, and potential delays.

## 5. Data Validation Checks

Before analysis, verify the following:

1. The expected number of unique patients is 500.
2. Every event has a valid event identifier.
3. Event order is valid within each patient journey.
4. Timestamps are valid and chronologically ordered within each journey.
5. All required columns are present.
6. Missing values and duplicate event identifiers are checked and documented.
7. Journey types and loop-back indicators are consistent with the event sequences.

## 6. Team Handoff

This schema serves as a reference for the BigQuery table, SQL validation queries, dbt transformations, and future process-mining analysis. Changes to column names or definitions should be communicated to the team to maintain consistency across project components.

**Note:** The schema describes the intended dataset structure. Confirm the actual CSV columns and data before treating all nine fields and the 500-patient count as verified.
