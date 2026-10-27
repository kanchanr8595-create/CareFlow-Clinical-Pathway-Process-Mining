# CareFlow — Event Sequence Validation

## 1. Objective
To verify that event-order values are consistent within each patient case in the CareFlow Clinical Pathway Process Mining dataset.

## 2. Validation Performed
A SQL query was executed in Google BigQuery to check whether each patient case starts at event order 1, contains consecutive event-order values, and has no duplicate event-order values. The validation grouped records by `case_id` and identified cases that did not meet these conditions.

## 3. Result
The query executed successfully and returned no rows. This means no patient cases were identified as violating the specified event-sequence checks.

## 4. Status
**Passed the specified event-sequence validation checks.**

## 5. Conclusion
The results indicate that the event-order values passed the defined sequence checks for all evaluated cases. This supports the reliability of the event-log sequence for further CareFlow analysis. Additional checks, such as timestamp ordering, may be performed separately if required.

**Tool Used:** Google BigQuery  
**Language:** SQL
