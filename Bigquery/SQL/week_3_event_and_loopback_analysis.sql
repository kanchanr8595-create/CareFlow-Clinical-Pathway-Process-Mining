-- CareFlow Project
--Week 3: Event Count and Loop-Back Analysis

#Query 1: Event Count by Activity

SELECT
  activity,
  COUNT(*) AS event_count,
  COUNTIF(is_loop_back = TRUE) AS loop_back_count
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY activity
ORDER BY event_count DESC;


#Query 2: Loop-Back Count by Activity
  SELECT
  case_id,
  event_order,
  activity,
  timestamp,
  is_loop_back
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
ORDER BY case_id, event_order
LIMIT 30;


#Query 3: Patient Cases with Loop-Back Activities

SELECT
  COUNT(DISTINCT case_id) AS cases_with_loop_back
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
WHERE is_loop_back = TRUE;
