CareFlow-Clinical-Pathway-Process-Mining


For our CareFlow – Clinical Pathway Process Mining project, 
we need to check three important things in our CSV dataset:
1.Duplicate values — whether the same records appear more than once.
2.Missing values — whether any cells are empty or contain null values.
3.Timestamp coding — whether date and time columns are stored correctly and can be used for process mining.

First, upload your careflow_synthetic_500_patients.csv file to your notebook and run:

pd.read_csv() loads your dataset.
df.head() displays the first five records.
df.shape tells you the number of rows and columns.
df.columns displays all column name


1.df.duplicated() checks whether entire rows are repeated.
2.event_id should normally identify each event uniquely.
3.The combination of case_id and event_order helps identify repeated event positions within a patient's journey.
For your dataset, the results are:
Check                                        Result
Complete duplicate rows                        0
Duplicate event IDs                            0
Duplicate case ID + event order combinations   0
Observation: No duplicates were detected in these checks. This is a good result for your data-validation task.
