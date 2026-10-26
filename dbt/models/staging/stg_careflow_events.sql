
 
WITH source_data AS (
    SELECT *
    FROM {{ source('careflow', 'raw_events') }}
),

cleaned AS (
    SELECT
        NULLIF(TRIM(CAST(case_id AS STRING)), '') AS case_id,
        NULLIF(TRIM(CAST(event_id AS STRING)), '') AS event_id,
        SAFE_CAST(event_order AS INT64) AS event_order,
        NULLIF(TRIM(activity), '') AS activity,
        SAFE_CAST(`timestamp` AS TIMESTAMP) AS event_timestamp,
        NULLIF(TRIM(department), '') AS department,
        NULLIF(TRIM(journey_type), '') AS journey_type,
        SAFE_CAST(is_loop_back AS BOOL) AS is_loop_back,
        NULLIF(TRIM(data_source), '') AS data_source
    FROM source_data
)

SELECT *
FROM cleaned
