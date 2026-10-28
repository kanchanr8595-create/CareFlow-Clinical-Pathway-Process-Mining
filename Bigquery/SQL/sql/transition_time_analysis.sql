WITH ordered_events AS (
    SELECT
        case_id,
        activity,
        timestamp AS event_timestamp,
        event_order,
        LEAD(activity) OVER (
            PARTITION BY case_id
            ORDER BY event_order
        ) AS next_activity,
        LEAD(timestamp) OVER (
            PARTITION BY case_id
            ORDER BY event_order
        ) AS next_timestamp
    FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway- process- mining`
)
SELECT
    activity,
    next_activity,
    COUNT(*) AS transition_count,
    AVG(
        TIMESTAMP_DIFF(
            next_timestamp,
            event_timestamp,
            MINUTE
        )
    ) AS avg_transition_minutes
FROM ordered_events
WHERE next_activity IS NOT NULL
  AND next_timestamp IS NOT NULL
GROUP BY activity, next_activity
ORDER BY avg_transition_minutes DESC
