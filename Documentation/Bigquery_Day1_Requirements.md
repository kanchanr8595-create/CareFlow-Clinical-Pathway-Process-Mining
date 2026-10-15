CareFlow Clinical Pathway Process Mining

BigQuery Setup and Testing Documentation

1. Purpose of BigQuery

Google BigQuery is a cloud-based data warehouse used to store and analyse data using SQL. In the CareFlow project, it is intended to store and inspect raw patient event-log data to support data validation and further process mining analysis.

2. Basic Storage Requirements

The basic requirements for storing raw event-log data in BigQuery include:

- A Google Cloud project.
- A BigQuery dataset.
- A table for the raw event-log data.
- The source CSV file.
- Appropriate column names and data types.
- Required permissions to load data and run queries.

3. Testing and Validation

The following SQL queries were used to inspect the data and check its basic structure.

Table Reference:
"care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining"

A. View and sort records

SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
ORDER BY case_id ASC, event_order ASC;

Purpose: Displays records in ascending order by case ID and event order.

B. Count total rows

SELECT COUNT(*) AS total_rows
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`;

Purpose: Counts the total number of records in the table.

C. View sample records

SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
LIMIT 10;

Purpose: Displays the first 10 records for inspection.

D. Check missing values

SELECT
  COUNT(*) AS total_rows,
  COUNTIF(case_id IS NULL) AS missing_case_id,
  COUNTIF(event_order IS NULL) AS missing_event_order
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`;

Purpose: Counts total rows and NULL values in the selected columns.

E. Inspect table and schema information

SELECT
  column_name,
  data_type
FROM `care-flow-clinical-pathway.careflow_dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'care-flow-clinical-pathway-process-mining'
ORDER BY ordinal_position;

Purpose: Lists the table's column names and data types in column order.

4. Conclusion

This work provided an initial understanding of BigQuery and its role in the CareFlow project. The project and dataset structure were explored, CSV event-log data was loaded into the table, and basic SQL queries were used to inspect records, count rows, check for missing values in selected columns, and review the schema. These checks form an initial step towards validating the raw data before further analysis. The query results and documentation should be reviewed by the team before being finalised and uploaded to GitHub.
