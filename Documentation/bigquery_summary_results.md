# CareFlow — BigQuery Summary Results

## 1. Project Details
- **Project:** CareFlow Clinical Pathway – Process Mining
- **Platform:** Google BigQuery
- **Dataset:** `careflow_dataset`
- **Table:** `care-flow-clinical-pathway-process-mining`

## 2. Table Verification
**Query:** Checked the available tables using `INFORMATION_SCHEMA.TABLES`.

**Result:** The CareFlow event-log table was found in the `careflow_dataset` dataset.

## 3. Schema Inspection
**Query:** Retrieved column names and data types using `INFORMATION_SCHEMA.COLUMNS`.

**Result:** The following columns were identified:

| Column | Data Type |
|---|---|
| `case_id` | STRING |
| `event_id` | STRING |
| `event_order` | INT64 |
| `activity` | STRING |
| `timestamp` | TIMESTAMP |
| `department` | STRING |
| `journey_type` | STRING |
| `is_loop_back` | BOOL |
| `data_source` | STRING |

## 4. Total Record Count
**Query:** Used `COUNT(*)` to count the records.

**Result:** 3,351 total rows.

## 5. Sample Data Preview
**Query:** Used `LIMIT 10` to display sample records.

**Result:** The first 10 rows were displayed successfully.

## 6. Missing Value Validation
**Query:** Checked for NULL values in `case_id` and `event_order`.

**Results:**
- Missing `case_id`: 0
- Missing `event_order`: 0

**Conclusion:** No missing values were found in these two columns.

## 7. Ascending Order Validation
**Query:** Sorted records using `ORDER BY case_id ASC, event_order ASC`.

**Result:** The records were displayed in ascending order by `case_id`, followed by `event_order`.

## 8. Overall Summary
The initial BigQuery setup and data exploration were completed. The table was verified, the schema was inspected, and 3,351 records were counted. The first 10 rows were displayed, missing values were checked, and the records were sorted by case ID and event order.

These checks establish an initial foundation for further CareFlow process mining analysis.
