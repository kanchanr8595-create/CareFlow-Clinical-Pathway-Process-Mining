CareFlow-Clinical-Pathway-Process-Mining


For our CareFlow – Clinical Pathway Process Mining project, 
we need to check three important things in our CSV dataset:

## 1.Duplicate values — whether the same records appear more than once.

## 2.Missing values — whether any cells are empty or contain null values.

## 3.Timestamp coding — whether date and time columns are stored correctly and can be used for process mining.

First, upload your careflow_synthetic_500_patients.csv file to your notebook and run:

1.pd.read_csv() loads our dataset.

2.df.head() displays the first five records.

3.df.shape tells us the number of rows and columns.

4.df.columns displays all column name


a.df.duplicated() checks whether entire rows are repeated.

b.event_id should normally identify each event uniquely.

c.The combination of case_id and event_order helps identify repeated event positions within a patient's journey.

For this dataset, the results are:
Check                                           Result
Complete duplicate rows                           0
Duplicate event IDs                               0
Duplicate case ID + event order combinations      0


Observation: No duplicates were detected in these checks.
