SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
ORDER BY case_id ASC, event_order ASC;


SELECT COUNT(*) AS total_rows
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`;


SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
LIMIT 10;


SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
WHERE case_id IS NULL
   OR event_order IS NULL
LIMIT 100;


 
 
SELECT
  table_catalog,
  table_schema,
  table_name
FROM
  `care-flow-clinical-pathway.careflow_dataset.INFORMATION_SCHEMA.TABLES`;


SELECT
  COUNT(*) AS total_rows,
  COUNTIF(case_id IS NULL) AS missing_case_id,
  COUNTIF(event_order IS NULL) AS missing_event_order
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`;






SELECT
  table_name,
  column_name,
  data_type
FROM
  `care-flow-clinical-pathway.careflow_dataset.INFORMATION_SCHEMA.COLUMNS`
ORDER BY
  table_name,
  ordinal_position;


