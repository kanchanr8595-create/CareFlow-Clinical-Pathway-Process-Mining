-- CareFlow: Event Sequence Validation

SELECT
  case_id,
  COUNT(*) AS total_events,
  MIN(event_order) AS first_event_order,
  MAX(event_order) AS last_event_order,
  COUNT(DISTINCT event_order) AS distinct_event_orders
FROM
  `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY
  case_id
HAVING
  MIN(event_order) != 1
  OR MAX(event_order) != COUNT(*)
  OR COUNT(DISTINCT event_order) != COUNT(*)
ORDER BY
  case_id;
