# BigQuery Analytical Data Preparation for Power BI

### Objective

To analyse patient activity distribution, department-wise event distribution, and patient journey duration in the CareFlow Clinical Pathway Process Mining dataset using BigQuery SQL. The analysis helps prepare structured information for further process analysis and Power BI dashboard development.

### Work Completed

- Executed activity-wise event count analysis using `GROUP BY` and `COUNT()` to identify the frequency of each patient activity.
- Performed department-wise event count analysis to understand how events are distributed across hospital departments.
- Calculated patient journey duration using `MIN(timestamp)`, `MAX(timestamp)`, and `TIMESTAMP_DIFF()` for each patient case.
- Exported the patient journey duration query results into a CSV file containing 500 patient cases.

### Query Results and Key Observations

**1. Activity-wise Event Count**

The query identified the total number of events recorded for each patient activity.

| Activity | Total Events |
|---|---:|
| Doctor Consultation | 609 |
| Discharge | 500 |
| Registration | 500 |
| Treatment | 500 |
| Triage | 500 |
| Lab Test | 488 |
| Imaging | 157 |
| Follow-up | 97 |

**Observation:** Doctor Consultation recorded the highest number of events with 609, while Follow-up recorded the lowest with 97.

**2. Department-wise Event Count**

The query calculated the distribution of events across different hospital departments.

| Department | Total Events |
|---|---:|
| Emergency | 1609 |
| Reception | 1000 |
| Laboratory | 488 |
| Radiology | 157 |
| Outpatient | 97 |

**Observation:** Emergency recorded the highest number of events with 1,609, followed by Reception with 1,000.

**3. Patient Journey Duration Analysis**

The query calculated the elapsed time between the first and last recorded event for each patient case using `MIN(timestamp)`, `MAX(timestamp)`, and `TIMESTAMP_DIFF()`.

**Analysis Results:**

- Total patient cases analysed: 500
- Average journey duration: 317.29 minutes
- Maximum journey duration: 651 minutes
- Minimum journey duration: 92 minutes

The complete patient journey duration results were exported into a CSV file containing the case ID, start time, end time, and journey duration in minutes.

### Outcome

The analysis provided an overview of patient activity frequency, department-wise event distribution, and patient journey duration. These results can support further process analysis and help prepare structured data for Power BI dashboard development.

### Output

- Activity-wise event count results documented in this report.
- Department-wise event count results documented in this report.
- Patient journey duration results exported as a CSV file for reference and further analysis.
