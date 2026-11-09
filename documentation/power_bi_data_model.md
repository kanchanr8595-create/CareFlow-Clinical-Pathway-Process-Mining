# CareFlow – Power BI Data Model and Relationships

## 1. Objective
The objective is to document the data model used for the CareFlow Power BI dashboard and explain how different datasets are connected.

## 2. Data Model Structure

The dashboard uses a fact-and-dimension model.

### Fact Table
- FactEvents: Contains patient event records, activity details, timestamps, departments, journey types, and transition information.

### Dimension Tables
- DimPatient: Contains patient-level journey information.
- DimActivity: Contains unique hospital activities.
- DimDepartment: Contains department details.
- DimJourneyType: Contains normal, delayed, loop-back, and complex journey categories.
- DimDate: Contains calendar information for date-based analysis.

## 3. Relationships

The following one-to-many relationships are defined:

| Dimension Table | Key | Fact Table Key |
|---|---|---|
| DimPatient | PatientID | PatientID |
| DimActivity | ActivityKey | ActivityKey |
| DimDepartment | DepartmentKey | DepartmentKey |
| DimJourneyType | JourneyTypeKey | JourneyTypeKey |
| DimDate | DateKey | DateKey |

Relationships use single-direction filtering from dimension tables to the FactEvents table.

## 4. Dashboard Measures

The dashboard includes:
- Total Patients
- Total Events
- Normal Patients
- Delayed Patients
- Loop-back Patients
- Complex Patients
- Average Events per Patient
- Average Transition Time
- Average Journey Duration

## 5. Dashboard Visualizations

- Patient Journey by Activity
- Journey Type Distribution
- Department-wise Event Analysis
- Loop-back Event Analysis
- Average Transition Time Analysis
- Patient Flow Process Map

## 6. Conclusion

The Power BI data model organizes patient event information into related tables, supporting structured analysis and interactive dashboard reporting.

Note: Relationships and measures should be verified in Power BI after importing the prepared datasets.
