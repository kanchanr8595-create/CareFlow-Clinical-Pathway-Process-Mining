# CareFlow — Mid-Project Review

## 1. Project Overview

CareFlow is a Clinical Pathway Process Mining project that aims to understand patient journeys through hospital treatment processes and identify delays, bottlenecks, and unusual activity sequences.

The project uses synthetic hospital event-log data and is designed for 500 patients. No real patient data is intended to be used.

## 2. Project Objectives

- Understand patient treatment journeys.
- Organize patient event-log data.
- Define data-quality and validation checks.
- Prepare the workflow for BigQuery data storage.
- Plan data cleaning and transformation using dbt.
- Identify pending tasks and dependencies before further analysis.

## 3. Work Completed by Kanchan

The following documentation files have been created in the `dev` branch:

- `dataset_schema.md`
- `patient_journey.md`
- `sample_data_notes.md`
- `data_validation_checklist.md`
- `event_standardization.md`
- `patient_sequence_test_cases.md`
- `week1_review.md`

The Day 9 integration review was also planned.

The presence of these files confirms that the related documentation is available. Actual data validation and execution must be reported separately based on verified results.

## 4. Team Progress

### Gouri — BigQuery

- Dataset and table status: [Update with verified status]
- CSV loading status: [Update with verified status]
- Query validation: [Update with actual results]
- Pending tasks: [List remaining tasks]

### Akshaya — Data Quality

- Missing-value checks: [Update with actual results]
- Duplicate-event checks: [Update with actual results]
- Timestamp-order checks: [Update with actual results]
- Pending tasks: [List remaining tasks]

### Alfiya — dbt

- Setup documentation: [Update with verified status]
- Project configuration: [Update with verified status]
- Staging model: [Update with verified status]
- Tests and execution: [Update with actual results]
- Pending tasks: [List remaining tasks]

## 5. Integration and Dependencies

The following dependencies need to be reviewed:

1. BigQuery source and table details are needed for the dbt source configuration.
2. Data-quality findings should guide the cleaning process.
3. The staging model should reference the agreed source table and column names.
4. Successful model execution and validation must be supported by actual results.

## 6. Current Challenges

Record the issues that have actually been identified by the team.

- BigQuery setup or loading issues: [Verified status]
- Data-quality issues: [Verified status]
- dbt setup or execution issues: [Verified status]
- Other blockers: [Details, if applicable]

If an item has not been checked, mark it as "Not yet verified."

## 7. Pending Work

- Complete outstanding data-quality checks.
- Confirm the BigQuery loading and validation status.
- Complete dbt setup and model execution where possible.
- Record actual results and resolve identified issues.
- Prepare the event log for further process-mining analysis.

Update these items according to the team's actual progress.

## 8. Next Phase

The next phase will focus on resolving outstanding dependencies, validating the available event log, improving the data-transformation workflow, and preparing the data for process-mining analysis.

Further analysis should begin only when the required data and validation results are available.

## 9. Final Status

The current project status is based on the documentation and evidence reviewed as of the date of this report.

Tasks without verified results remain pending or unverified. This report does not claim that BigQuery loading, automated validation, or dbt execution succeeded unless the team has confirmed those results.

Review date: 23 October 2026
