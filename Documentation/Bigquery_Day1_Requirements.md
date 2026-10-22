# BigQuery Setup and Testing

## Purpose
Set up and explore Google BigQuery for the CareFlow Clinical Pathway Process Mining project to inspect healthcare event-log data and prepare it for further analysis. The raw healthcare event-log dataset contains records of activities performed during patient journeys. Each record represents an event in the patient healthcare process. This data helps us understand the sequence of activities and support further process mining analysis.

## Planned Setup

- Understand the CareFlow Clinical Pathway Process Mining project requirements.
- Identify the raw healthcare event-log dataset and understand its purpose.
- Identify the Google Cloud project, BigQuery dataset, and destination table.
- Review the expected table schema, column names, and data types.
- Prepare SQL queries to inspect records, count events, check missing values, and validate event ordering.
- Plan basic data-quality checks to prepare the dataset for further process mining analysis.

## Completed Setup

- Explored the Google Cloud project and BigQuery dataset.
- Accessed the raw healthcare event-log table.
- Verified the table name and dataset structure.
- Reviewed the nine column names and their data types.
- Executed SQL queries to inspect sample records and review event ordering.
- Verified that the table contains 3,351 records.
- Checked missing values in key columns and confirmed that `case_id` and `event_order` each have zero missing values.
- Previewed the first 10 records.
- Performed initial data validation to understand the event-log structure and assess data availability for further process mining analysis.

## Work Completed
- Explored the Google Cloud project and BigQuery dataset.
- Loaded and accessed the raw healthcare event-log dataset.
- Verified the table name and dataset structure.
- Reviewed column names and data types.
- Prepared SQL queries to inspect and sort records.
- Checked the total number of records and investigated missing values in key columns.
- Performed initial data validation to support further process mining analysis.

## CSV Data Loading Procedure

1. Open Google Cloud Console and navigate to BigQuery.
2. Select the Google Cloud project `care-flow-clinical-pathway`.
3. Open the dataset `careflow_dataset`.
4. Load the available CareFlow CSV event-log data into the raw BigQuery table.
5. Verify the destination table and its available columns.
6. Run a sample query to confirm that records can be retrieved successfully.
7. Check the BigQuery load-job status and confirm whether any loading errors were reported.

### Loading Status

CSV loading was completed successfully, and no loading errors were reported.

## Purpose of Validation
- Understand the structure of the healthcare event-log dataset.
- Verify data availability and basic data quality.
- Identify missing values in important fields.
- Prepare the dataset for further process mining analysis.

## Data Privacy
Only synthetic or anonymized sample data should be used in this project. No real patient-identifiable information should be uploaded or shared.

## Outcome
Completed the initial BigQuery setup and data exploration. Basic SQL queries were prepared to inspect the dataset, review its schema, count records, and check for missing values. The results can be reviewed by the team before proceeding with further analysis.
