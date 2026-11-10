# CareFlow Clinical Pathway – Process Mining

## Project Overview

CareFlow Clinical Pathway – Process Mining is a data analytics project focused on exploring healthcare event-log data to understand patient journeys and clinical workflows. The project uses event-level records to examine the sequence of activities, departments involved, transition times, and repeated steps in a patient's journey.

The project aims to prepare, validate, and analyse structured healthcare event data to support process mining, data transformation, and dashboard development.

## Project Objectives

- Set up a Google BigQuery environment for the CareFlow dataset.
- Load and explore healthcare event-log data.
- Review the dataset schema and column data types.
- Validate record counts and check missing values in important fields.
- Analyse patient activity distribution and department-wise event distribution.
- Examine patient event sequences and journey duration.
- Calculate activity transition times and identify potential bottlenecks.
- Organize SQL queries, analytical results, and documentation.
- Prepare structured data for further data-quality checks, dbt modelling, process mining, and Power BI dashboard development.

## Tools and Technologies

- **Google BigQuery** – Cloud data storage, SQL queries, data exploration, and validation.
- **SQL** – Data analysis, event counting, transition analysis, and patient journey analysis.
- **dbt** – Data transformation and modelling as part of the team workflow.
- **Git and GitHub** – Version control, project documentation, and team collaboration.
- **Microsoft Excel / CSV** – Reviewing and organizing exported query results.

## Dataset Details

- **Google Cloud Project:** `care-flow-clinical-pathway`
- **Dataset:** `careflow_dataset`
- **Source Table:** `care-flow-clinical-pathway-process-mining`
- **Total Records:** 3,351
- **Unique Cases:** 500
- **Total Columns:** 9

The dataset contains event-level information representing clinical pathway activities and their sequence.

## Dataset Schema

| Column | Data Type | Description |
|---|---|---|
| case_id | STRING | Identifier for a patient journey or case |
| event_id | STRING | Identifier for an event |
| event_order | INT64 | Sequence of an event within a case |
| activity | STRING | Clinical or workflow activity |
| timestamp | TIMESTAMP | Date and time associated with an event |
| department | STRING | Department associated with the event |
| journey_type | STRING | Classification of the clinical journey |
| is_loop_back | BOOL | Indicates whether an event represents a loop-back |
| data_source | STRING | Source associated with the event record |

## Work Completed – BigQuery Setup and Data Validation

My contribution focuses on BigQuery setup, data loading, dataset exploration, SQL-based validation, analytical queries, and documentation.

### 1. BigQuery Setup and Data Loading

- Set up and accessed the Google BigQuery project and dataset.
- Loaded the source CSV data into a BigQuery table.
- Reviewed the table schema, column names, and data types.
- Retrieved sample records to inspect the loaded data.

### 2. Initial Data Validation

- Executed SQL queries to verify the total record count.
- Checked the number of unique patient cases.
- Checked missing values in important fields such as `case_id` and `event_order`.
- Reviewed event ordering using `case_id` and `event_order`.
- Performed event-sequence validation to check whether patient cases followed the expected event-order sequence.
- Documented the validation queries and results.

### 3. Patient Case-wise Event Count and Journey Analysis

- Calculated the total number of events for each patient case using `COUNT()` and `GROUP BY`.
- Retrieved sample patient cases to examine their event distribution.
- Selected individual patient cases and reviewed their complete event sequences.
- Examined event IDs, event order, activities, timestamps, and departments to understand patient journey progression.

### 4. Activity Transition and Bottleneck Analysis

- Used SQL window functions such as `LEAD()` to examine transitions between consecutive patient activities.
- Calculated transition counts and average transition times in minutes.
- Grouped transitions by current and next activities.
- Identified transitions with higher average recorded durations for further investigation.

**Selected Transition Results**

| Activity Transition | Transition Count | Average Time (Minutes) |
|---|---:|---:|
| Imaging → Treatment | 96 | 96.09 |
| Doctor Consultation → Treatment | 91 | 90.04 |
| Lab Test → Treatment | 313 | 88.22 |
| Triage → Doctor Consultation | 500 | 82.29 |
| Registration → Triage | 500 | 20.06 |

These results highlight transitions with relatively higher recorded average durations. They represent observed event-log intervals and do not independently establish the cause of delays or their clinical impact.

### 5. Activity-wise Event Count Analysis

Executed SQL queries using `GROUP BY`, `COUNT()`, and `ORDER BY` to calculate the total number of events for each activity.

| Activity | Total Events |
|---|---:|
| Doctor Consultation | 609 |
| Discharge | 500 |
| Registration | 500 |
| Treatment | 500 |
| Triage | 500 |
| Lab Test | 488 |
| Imaging | 157 |
| Follow-up | 97 |

**Key Observation:** Doctor Consultation recorded the highest number of events with 609, while Follow-up recorded the lowest with 97.

### 6. Department-wise Event Count Analysis

Analysed event distribution across hospital departments using SQL aggregation.

| Department | Total Events |
|---|---:|
| Emergency | 1,609 |
| Reception | 1,000 |
| Laboratory | 488 |
| Radiology | 157 |
| Outpatient | 97 |

**Key Observation:** Emergency recorded the highest number of events with 1,609, followed by Reception with 1,000.

### 7. Patient Journey Duration Analysis

Calculated the elapsed time between the first and last recorded event for each patient case using `MIN(timestamp)`, `MAX(timestamp)`, and `TIMESTAMP_DIFF()`.

**Analysis Results**

- Total patient cases analysed: 500
- Average journey duration: 317.29 minutes
- Maximum journey duration: 651 minutes
- Minimum journey duration: 92 minutes

The query results were exported into a CSV file containing the patient case ID, start time, end time, and journey duration in minutes.

## Validation Results

| Validation Check | Result |
|---|---:|
| Total records | 3,351 |
| Unique cases | 500 |
| Total columns | 9 |
| Missing case_id values | 0 |
| Missing event_order values | 0 |
| Sample record inspection | First 10 records reviewed |
| Event sequence validation | No violations found in the specified checks |

## Example SQL Queries

### 1. Count Total Records

```sql
SELECT COUNT(*) AS total_records
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`;
```

### 2. Activity-wise Event Count

```sql
SELECT
  activity,
  COUNT(*) AS total_events
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
GROUP BY activity
ORDER BY total_events DESC;
```

### 3. Department-wise Event Count

```sql
SELECT
  department,
  COUNT(*) AS total_events
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
GROUP BY department
ORDER BY total_events DESC;
```

### 4. Patient Journey Duration

```sql
SELECT
  case_id,
  MIN(timestamp) AS start_time,
  MAX(timestamp) AS end_time,
  TIMESTAMP_DIFF(
    MAX(timestamp),
    MIN(timestamp),
    MINUTE
  ) AS journey_duration_minutes
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
GROUP BY case_id
ORDER BY journey_duration_minutes DESC;
```

### 5. Preview Sample Records

```sql
SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
LIMIT 10;
```

## Project Workflow

1. **Data Setup:** Create the BigQuery dataset and load the source event-log data.
2. **Schema Exploration:** Inspect column names, data types, and table structure.
3. **Initial Validation:** Check record counts, sample records, and missing values.
4. **Event Sequence Validation:** Review patient event ordering and sequence consistency.
5. **Patient Journey Analysis:** Examine patient-level event counts and individual event sequences.
6. **Transition Analysis:** Calculate transition times between consecutive activities and identify potential bottlenecks.
7. **Analytical Data Preparation:** Calculate activity-wise counts, department-wise counts, and patient journey durations.
8. **Data Transformation:** Prepare data for staging models and transformations through the team's dbt workflow.
9. **Process Mining and Visualization:** Support further clinical pathway analysis and Power BI dashboard development.
10. **Documentation and Collaboration:** Maintain SQL queries, analytical results, validation evidence, and project updates in GitHub.

## Data Privacy

Healthcare-related data should be handled according to the project's privacy requirements. Avoid publishing personally identifiable or confidential patient information in the repository, screenshots, or documentation. Ensure that any exported CSV files and sample records are approved for sharing within the project repository.

## Current Contribution

**Role: BigQuery Setup, Data Validation, and SQL Analysis**

My responsibilities and completed contributions include:

- BigQuery project, dataset, and table setup.
- Source CSV data loading and schema inspection.
- Initial record-count and missing-value validation.
- Event-sequence validation.
- Patient case-wise event count and journey analysis.
- Activity transition-time and bottleneck analysis.
- Activity-wise and department-wise event count analysis.
- Patient journey duration calculation and CSV result export.
- SQL query organization and GitHub documentation for team review.

The broader project also includes dbt modelling, process mining, and Power BI dashboard development as part of the team's workflow.

## Conclusion

The BigQuery work has progressed from initial data setup and validation to patient-level analysis, activity transition analysis, bottleneck identification, and analytical data preparation. These tasks provide a structured foundation for understanding patient journey patterns and support the team's subsequent data transformation, process mining, and Power BI dashboard development.
