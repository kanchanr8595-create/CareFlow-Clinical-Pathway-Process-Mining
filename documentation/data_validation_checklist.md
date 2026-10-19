# CareFlow Data Validation Checklist

## 1. Purpose

This checklist defines the initial quality checks for the CareFlow synthetic patient event log. It helps the team identify missing, duplicate, or incorrectly ordered event records.

## 2. Validation Checks

| Check | What to Verify | Status |
|---|---|---|
| Required columns | All expected columns are present | Pending |
| Patient IDs | Each event has a case ID | Pending |
| Event IDs | Event IDs are not duplicated | Pending |
| Missing values | Required fields are not blank | Pending |
| Timestamps | Dates and times follow a consistent format | Pending |
| Event order | Events follow the correct sequence for each patient | Pending |
| Journey types | Journey types use the expected categories | Pending |
| Loop-back flag | Repeated consultation events are flagged correctly | Pending |

## 3. Important Note

These checks are planned but have not yet been confirmed through an executed validation script. Results must be updated after the dataset is tested.

## 4. Next Steps

1. Run the validation checks when a Python environment is available.
2. Record the actual results and any issues found.
3. Share relevant data-quality findings with the CareFlow team.
4. Recheck the dataset after any corrections.

## 5. Expected Outcome

A documented list of data-quality checks and verified results that can support the CareFlow data preparation workflow.
