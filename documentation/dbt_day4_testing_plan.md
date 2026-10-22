# CareFlow — Day 4: dbt Testing Plan

## 1. Objective

The objective is to define data-quality checks for the CareFlow event log before the initial dbt model is executed.

## 2. Required Fields

The following fields should be checked for missing values:

- case_id
- event_id
- event_order
- activity
- timestamp

## 3. Uniqueness Checks

- Check whether event_id is unique across the dataset.
- Confirm the uniqueness rule with the source data design before applying the test.
- Do not assume that case_id is unique because one patient can have multiple events.

## 4. Timestamp Checks

- Confirm that timestamps are valid.
- Check that events follow the expected sequence for each patient.
- Investigate invalid or missing timestamps before transformation.

## 5. Event Sequence Checks

- Check event_order within each case_id.
- Identify repeated activities and loop-back events.
- Do not automatically remove repeated activities because they may be important for process mining.

## 6. Loop-Back Checks

- Confirm that is_loop_back contains valid Boolean values.
- Review loop-back events separately from normal events.
- Preserve valid loop-back records in the cleaned event log.

## 7. Raw and Clean Data Comparison

After dbt execution:

- Compare raw and cleaned event counts.
- Check whether required columns are preserved.
- Investigate unexpected record loss.
- Verify that transformed timestamps and identifiers are valid.

## 8. Current Status

Day 4: Testing requirements documented.

Pending:
- BigQuery raw table availability.
- dbt model execution.
- Automated test results.
- Raw-versus-clean data comparison.

Tests will be marked complete only after execution and verification.
