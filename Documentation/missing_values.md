CareFlow – Data Cleaning and Validation

Objective: To assess the quality and consistency of the clinical pathway event log before performing process mining analysis.

## Total records: 3,351
## Total columns: 9
## Total missing cells: 0


# Column           Missing values
## 1.case_id               0
## 2.event_id              0
## 3.event_order           0
## 4.activity              0
## 5.timestamp             0
## 6.department            0
## 7.journey_type          0
## 8.is_loop_back          0
## 9.data_source           0



Observation: No missing values were detected in any column. Therefore, you do not need to fill or remove missing values at this stage.

Note: isnull() detects standard missing values such as NaN and None. If your data uses empty strings or text such as "NA" to represent missing values, those should be checked separately.

Missing Value Validation: Examined all nine columns for missing values. No missing values were detected across the 3,351 records.
