-- PROJECT: CareFlow Clinical Pathway - Process Mining
-- PLATFORM: Google BigQuery
-- PURPOSE: Count unique clinical pathway cases

-- STEP 1: Count total unique cases
SELECT
  COUNT(DISTINCT case_id) AS total_unique_cases
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`;

-- STEP 2: Count records for each case
SELECT
  case_id,
  COUNT(*) AS total_events
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
WHERE
  case_id IS NOT NULL
GROUP BY
  case_id
ORDER BY
  total_events DESC;
