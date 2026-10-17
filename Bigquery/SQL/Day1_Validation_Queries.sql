PROJECT: Care Flow Clinical Pathway - Process Mining
-- PLATFORM: Google BigQuery

-- STEP 1: CREATE DATASET
CREATE SCHEMA IF NOT EXISTS
`care-flow-clinical-pathway.careflow_dataset`;


-- STEP 2: CREATE TABLE AND IMPORT CSV DATA
-- Dataset: careflow_dataset
-- Create the destination table in BigQuery.
-- Upload the raw CSV file using Create table > Upload.
-- Configure the destination table and schema.
-- These steps have already been completed through the BigQuery interface.


-- STEP 3: CHECK AVAILABLE TABLES
SELECT
  table_catalog,
  table_schema,
  table_name
FROM
  `care-flow-clinical-pathway.careflow_dataset.INFORMATION_SCHEMA.TABLES`;


-- STEP 4: CHECK TABLE COLUMNS AND DATA TYPES
SELECT
  table_name,
  column_name,
  data_type
FROM
  `care-flow-clinical-pathway.careflow_dataset.INFORMATION_SCHEMA.COLUMNS`
ORDER BY
  table_name,
  ordinal_position;


-- STEP 5: SORT DATA BY CASE ID AND EVENT ORDER
SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
ORDER BY case_id ASC, event_order ASC;


-- STEP 6: COUNT TOTAL ROWS
SELECT COUNT(*) AS total_rows
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`;


-- STEP 7: VIEW FIRST 10 ROWS
SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
LIMIT 10;


-- STEP 8: CHECK MISSING CASE IDs AND EVENT ORDER
SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
WHERE case_id IS NULL
   OR event_order IS NULL
LIMIT 100;


-- STEP 9: COUNT TOTAL ROWS AND MISSING VALUES
SELECT
  COUNT(*) AS total_rows,
  COUNTIF(case_id IS NULL) AS missing_case_id,
  COUNTIF(event_order IS NULL) AS missing_event_order
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`;
