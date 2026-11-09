SELECT
  activity,
  COUNT(*) AS total_events
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY activity
ORDER BY total_events DESC;
