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


## Day 3 — Schema Inspection and SQL Validation

### Completed Tasks

- Created the BigQuery dataset and set up the raw event-log table.
- Loaded the CareFlow CSV data into BigQuery.
- Inspected the available tables and verified the table schema.
- Prepared SQL queries to inspect and sort event records by `case_id` and `event_order`.
- Prepared and executed a query to count total event records.
- Retrieved the first 10 sample records for inspection.
- Checked for missing `case_id` and `event_order` values.
- Prepared a query to count distinct cases/patient journeys.
- Added comments explaining the purpose of each SQL query.
- Documented the CSV loading procedure and basic validation workflow.

### Results Recorded

- Total records: 3,351
- Missing `case_id` values: 0
- Missing `event_order` values: 0
- Source CSV and BigQuery row counts: 3,351 each; difference: 0

### Status

Initial BigQuery setup, CSV loading documentation, and basic validation query preparation are completed. The distinct-case count and any additional data-quality findings should be recorded using the actual BigQuery query results.

---

## Day 4 — Data Loading and Validation Review

### Completed Tasks

- Inspected the existing BigQuery table.
- Recorded the schema and row-count results.
- Reviewed missing-value checks for key columns.
- Documented the CSV loading procedure.
- Compared source CSV and BigQuery row counts; both contained 3,351 data rows.
- Confirmed that no loading errors or permission issues were encountered.

**Status:** BigQuery table inspection, CSV loading documentation, row-count comparison, and basic validation checks completed. Further data-quality checks may be performed as required.

---

## Day 5 — BigQuery Table Inspection

### Verified Results

- BigQuery table is accessible.
- Total records found: 3,351.
- First 10 records retrieved successfully.
- No missing `case_id` values found.
- No missing `event_order` values found.
- CSV data was loaded successfully into BigQuery.
- No loading errors or permission issues were reported.
- The source CSV row count matches the BigQuery table row count: 3,351.

### Completed Tasks

- Confirmed that the destination table was created.
- Verified the loaded row count.
- Previewed sample records.
- Documented the CSV loading procedure and validation results.

**Status:** Day 5 — BigQuery Table Inspection completed.

---

## Day 6 — Week 1 Progress Summary

### Completed Tasks
- Explored the BigQuery project and dataset.
- Documented the dataset schema.
- Executed basic SQL validation queries.
- Recorded row-count, sample-data, and missing-value results.
- Prepared setup and validation documentation.

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

---

## Overall Status

The initial BigQuery exploration, schema documentation, and basic SQL validation have been completed and documented.

### Verified Results
- **Total records:** 3,351
- **Schema columns documented:** 9
- **Missing `case_id` values:** 0
- **Missing `event_order` values:** 0
- **Sample records:** 10 retrieved successfully



