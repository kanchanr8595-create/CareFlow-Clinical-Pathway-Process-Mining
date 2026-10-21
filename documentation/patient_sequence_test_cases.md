# CareFlow — Day 8 Patient Journey Test Cases

## 1. Objective

The objective of this document is to define test cases for checking patient event sequences and data quality in the CareFlow synthetic hospital event log.

The project dataset is designed for 500 patients. It contains synthetic data only and does not use real patient information.

## 2. Expected Patient Journey

A normal patient journey may follow this sequence:

1. Registration
2. Triage
3. Doctor Consultation
4. Lab Test or Imaging, if required
5. Treatment
6. Discharge
7. Follow-up, if applicable

The exact sequence may vary depending on the patient's journey type and required treatment.

## 3. Patient Journey Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Check whether each event has a case ID | Every event should have a case ID |
| TC02 | Check event order for each patient | Event order should be consistent with the recorded journey |
| TC03 | Check timestamps within each patient journey | Events should follow chronological order |
| TC04 | Check missing activity names | Activity names should not be blank |
| TC05 | Check missing timestamps | Timestamps should not be blank |
| TC06 | Check duplicate events | Possible duplicates should be identified and reviewed |
| TC07 | Check normal patient journey | Events should follow a reasonable treatment sequence |
| TC08 | Check delayed patient journey | Delays should be reviewed without automatically marking the journey invalid |
| TC09 | Check loop-back journey | Repeated activities should be reviewed as possible loop-backs |
| TC10 | Check journey type | Each event should have a valid journey type |

## 4. Data Quality Rules

- Case IDs and event IDs should be present.
- Activity names should use consistent spelling.
- Timestamps should use a consistent format.
- Events for the same patient should be reviewed in chronological order.
- Duplicate records should be investigated before removal.
- Repeated consultations may be valid loop-backs and should not automatically be deleted.
- Delayed journeys should be reviewed separately from invalid journeys.

## 5. Validation Status

The test cases and expected results have been documented.

Actual validation results are pending until the CSV dataset is checked using suitable data-validation steps. No test should be marked as passed unless it has actually been performed.

## 6. Next Steps

1. Run the validation checks on the synthetic event log.
2. Record the actual results for each test case.
3. Investigate missing values, duplicate events, timestamp issues, and unusual patient sequences.
4. Share relevant findings with the team for further cleaning and transformation.
