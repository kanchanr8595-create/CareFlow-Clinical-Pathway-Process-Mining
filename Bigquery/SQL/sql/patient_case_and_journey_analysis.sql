-- CareFlow Clinical Pathway Process Mining
-- Patient Case-wise Event Count and Journey Analysis

-- Query 1: Patient Case-wise Event Count Analysis

SELECT
    case_id,
    COUNT(*) AS total_events
FROM
    `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
GROUP BY
    case_id
ORDER BY
    case_id
LIMIT 10;


-- Query 2: Individual Patient Journey Analysis

SELECT
    case_id,
    event_id,
    event_order,
    activity,
    timestamp,
    department,
    journey_type,
    is_loop_back
FROM
    `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
WHERE
    case_id = 'YOUR_CASE_ID'
ORDER BY
    event_order;
