
SELECT
    case_id,
    event_id,
    event_order,
    activity,
    event_timestamp,
    department,
    journey_type,
    is_loop_back,
    data_source
FROM {{ ref('stg_careflow_events') }}
WHERE case_id IS NOT NULL
  AND event_id IS NOT NULL
  AND activity IS NOT NULL
  AND event_timestamp IS NOT NULL
