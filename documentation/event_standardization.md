# CareFlow — Event Data Standardization

## 1. Purpose

The purpose of event data standardization is to keep activity names, timestamps, and event fields consistent across the CareFlow dataset. A consistent format makes it easier to validate patient journeys and prepare the data for BigQuery and dbt.

## 2. Existing Event Log Fields

The current CSV is documented with the following fields:

| Field | Purpose |
|---|---|
| case_id | Identifies a patient's journey |
| event_id | Identifies an individual event |
| event_order | Shows the order of events in a journey |
| activity | Names the hospital activity |
| timestamp | Records the event date and time |
| department | Identifies the responsible department |
| journey_type | Describes the generated journey pattern |
| is_loop_back | Indicates a repeated consultation when applicable |
| data_source | Identifies the source of the record |

## 3. Proposed Standardization Rules

### Activity Names
- Use consistent spelling and capitalization.
- Use the same name for the same hospital activity throughout the dataset.
- Review unexpected variations before making changes.

### Timestamps
- Use one consistent date-time format.
- Ensure timestamps can be interpreted as dates and times.
- Check that event timestamps follow the intended order within each patient journey.

### Event Order
- Keep event_order consistent with the sequence of events for each patient.
- Review repeated activities to ensure they are represented correctly.

### Identifiers
- Each event should have an event_id.
- Each event should be linked to a case_id.
- Check for duplicate event IDs during validation.

## 4. Current Verification Status

These rules are proposed for review. The dataset has not yet been verified against every rule by running an automated validation script.

| Item | Status |
|---|---|
| Existing column names documented | Documented |
| Activity-name consistency | Pending verification |
| Timestamp format consistency | Pending verification |
| Event-order correctness | Pending verification |
| Duplicate event IDs | Pending verification |
| Loop-back flags | Pending verification |

## 5. Next Steps

1. Review the actual CSV and Python generator.
2. Run validation checks in a Python environment when available.
3. Record any inconsistent values and correct them only after review.
4. Coordinate with the team on BigQuery column types and dbt staging-model naming.
5. Update this document with verified results.

## 6. Expected Outcome

A consistent event-log format that can be validated and prepared for the CareFlow data pipeline.
