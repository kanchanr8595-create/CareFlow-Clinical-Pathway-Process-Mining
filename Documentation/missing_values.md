CareFlow – Data Cleaning and Validation

Objective: To assess the quality and consistency of the clinical pathway event log before performing process mining analysis.

Total records: 3,351
Total columns: 9
Total missing cells: 0


Column           Missing values
case_id               0
event_id              0
event_order           0
activity              0
timestamp             0
department            0
journey_type          0
is_loop_back          0
data_source           0
Total records: 3,351


Observation: No missing values were detected in any column. Therefore, you do not need to fill or remove missing values at this stage.

Note: isnull() detects standard missing values such as NaN and None. If your data uses empty strings or text such as "NA" to represent missing values, those should be checked separately.

Missing Value Validation: Examined all nine columns for missing values. No missing values were detected across the 3,351 records.
