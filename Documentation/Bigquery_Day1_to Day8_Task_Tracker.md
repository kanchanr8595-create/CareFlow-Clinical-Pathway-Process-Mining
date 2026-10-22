# CareFlow Clinical Pathway Process Mining
## BigQuery Task Summary — Day 1 to Day 8

### Project Details
- **Branch:** `development_gaouri`
- **Google Cloud Project:** `care-flow-clinical-pathway`
- **Dataset:** `careflow_dataset`
- **Table:** `care-flow-clinical-pathway-process-mining`

---

## Day 1 — BigQuery Requirements and Initial Exploration

### Completed Tasks
- Reviewed the CareFlow project objective and the role of BigQuery in process mining.
- Explored the Google Cloud project and BigQuery dataset.
- Identified the existing BigQuery table.
- Reviewed the event-log dataset structure.
- Documented the initial setup plan and completed exploration.

### Existing Documentation
- `BigQuery Setup and Testing.md`
- `CareFlow Dataset Schema`
- `BigQuery Summary Results`

**Status:** Initial BigQuery exploration and setup documentation completed.

---

## Day 2 — Dataset and Table Structure

### Completed Tasks
- Documented the dataset overview and column definitions.
- Recorded the nine schema columns and their data types.
- Documented the existing BigQuery table details.
- Recorded available row-count and missing-value validation results.

### Pending Tasks
- Document the actual CSV loading procedure, if not already recorded.
- Compare the source CSV row count with the BigQuery table row count, if the source file is available.
- Record any actual loading errors or permission issues, if encountered.

**Status:** Schema documentation completed; additional loading verification remains pending.

---

## Day 3 — Schema Inspection and SQL Validation

### Completed Tasks
- Reviewed the table schema and data types.
- Retrieved the first 10 sample records.
- Executed a total row-count query.
- Checked missing values in `case_id` and `event_order`.
- Reviewed event records ordered by `case_id` and `event_order`.

### Verified Results
- **Total records:** 3,351
- **Sample records retrieved:** 10
- **Missing `case_id` values:** 0
- **Missing `event_order` values:** 0

**Status:** Basic SQL validation completed.

---

## Day 4 — Data Loading and Validation Review

### Completed Tasks
- Inspected the existing BigQuery table.
- Recorded the schema and row-count results.
- Reviewed missing-value checks for key columns.

### Pending Tasks
- Compare source and destination row counts, if the source CSV is available.
- Confirm and document the actual CSV loading method.
- Record any loading errors or blockers, if applicable.

**Status:** Existing table inspection completed; loading verification remains pending.

---

## Day 5 — BigQuery Table Inspection

### Verified Results
- BigQuery table is accessible.
- Total records found: 3,351.
- First 10 records retrieved successfully.
- No missing `case_id` values found.
- No missing `event_order` values found.

### Pending Task
- Confirm whether any additional CSV loading attempt was required and document the result only if the attempt was performed.

**Status:** Basic table inspection completed.

---

## Day 6 — Week 1 Progress Summary

### Completed Tasks
- Explored the BigQuery project and dataset.
- Documented the dataset schema.
- Executed basic SQL validation queries.
- Recorded row-count, sample-data, and missing-value results.
- Prepared setup and validation documentation.

### Remaining Checks
- Confirm source-to-destination row-count consistency.
- Check for unresolved data-loading issues.
- Review the team checklist and update the status of each requirement.

**Status:** Initial setup and validation work documented.

---

## Day 7 — Event Data Consistency Requirements

### Checks to Perform
- Confirm that `case_id` identifies the intended case or patient journey.
- Review `event_id` and `activity` values for consistency.
- Check `event_order` consistency within each case.
- Verify that `timestamp` values align with the intended event sequence.
- Review `department`, `journey_type`, `is_loop_back`, and `data_source` values.
- Record any inconsistent or missing values identified.

**Status:** Schema documented; additional data-consistency checks require verification.

---

## Day 8 — Final Review and Team Handover

### Completed Work
- Documented the Google Cloud project, dataset, and table details.
- Recorded the nine schema columns and their data types.
- Recorded the total row count of 3,351.
- Recorded missing-value results for `case_id` and `event_order`.
- Confirmed that sample records were retrieved successfully.
- Prepared the existing setup, schema, and validation documentation.

### Handover Notes
- Share the existing schema and validation documents with the team.
- Identify any remaining data-loading or data-quality checks.
- Document unresolved issues and next steps.
- Confirm the final task status with the team leader.

---

## Overall Status

The initial BigQuery exploration, schema documentation, and basic SQL validation have been completed and documented.

### Verified Results
- **Total records:** 3,351
- **Schema columns documented:** 9
- **Missing `case_id` values:** 0
- **Missing `event_order` values:** 0
- **Sample records:** 10 retrieved successfully

### Remaining Actions
- Verify source-to-destination row-count consistency, if the source CSV is available.
- Confirm the actual CSV loading procedure.
- Perform and document the additional event-data consistency checks.
- Update pending items based on the actual results.
- Confirm completion with the team leader.

**Final Note:** Only mark the remaining checks as completed after verifying the actual work and results in BigQuery.
