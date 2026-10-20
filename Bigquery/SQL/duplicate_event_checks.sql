-- PROJECT: CareFlow Clinical Pathway - Process Mining
-- PLATFORM: Google BigQuery
-- PURPOSE: Identify potential duplicate event records

-- STEP 1: Check duplicate case_id and event_order combinations
SELECT
  case_id,
  event_order,
  COUNT(*) AS duplicate_count
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY
  case_id,
  event_order
HAVING
  COUNT(*) > 1
ORDER BY
  duplicate_count DESC;

-- STEP 2: Count repeated case_id and event_order combinations
SELECT
  COUNT(*) AS duplicate_combinations
FROM (
  SELECT
    case_id,
    event_order
  FROM
    `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
  GROUP BY
    case_id,
    event_order
  HAVING
    COUNT(*) > 1
);
