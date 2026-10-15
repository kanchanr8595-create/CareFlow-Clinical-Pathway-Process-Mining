# CareFlow Dataset Schema

## 1. Purpose

This document describes the structure of the synthetic CareFlow patient event-log dataset. It helps the team understand the columns before loading the data into BigQuery and transforming it with dbt.

## 2. Dataset Overview

- Dataset file: `careflow_synthetic_500_patients.csv`
- Expected patients: 500
- Data type: Synthetic clinical pathway event log
- Main purpose: To study patient journeys, waiting times, repeated activities, and potential hospital bottlenecks.
- Privacy: No real patient data is used by the generator.

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
| `data_source` | Identifies the records as synthetic |

## 4. Data Usage

- Python generates the synthetic event log.
- BigQuery can store the event-log records for analysis.
- dbt can be used to create cleaned and transformed models.
- Process-mining analysis can use the ordered activities and timestamps to investigate delays and repeated steps.

## 5. Validation Checks

Before using the dataset, check:

1. The expected number of unique patients is 500.
2. Each event has an event identifier.
3. Event order is valid within each patient journey.
4. Timestamps are valid and chronologically ordered within each journey.
5. Required columns are present.
6. Missing values and duplicate event identifiers are checked and documented.

## 6. Team Handoff

This schema is a reference for the BigQuery table structure, dbt transformations, and future process-mining analysis. Any changes to column names should be communicated to the team.
