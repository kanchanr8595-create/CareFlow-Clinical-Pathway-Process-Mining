SELECT
  case_id,
  event_id,
  COUNT(*) AS duplicate_count
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY case_id, event_id
HAVING COUNT(*) > 1;

SELECT
  activity,
  COUNT(*) AS total_events
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY activity
ORDER BY total_events DESC;
