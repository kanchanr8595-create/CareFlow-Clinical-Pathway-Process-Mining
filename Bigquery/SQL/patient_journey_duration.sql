SELECT
  case_id,
  MIN(timestamp) AS start_time,
  MAX(timestamp) AS end_time,
  TIMESTAMP_DIFF(
    MAX(timestamp),
    MIN(timestamp),
    MINUTE
  ) AS journey_duration_minutes
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY case_id
ORDER BY journey_duration_minutes DESC;
