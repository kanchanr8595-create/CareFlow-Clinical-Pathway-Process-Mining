# CareFlow — Patient Journey Documentation

## 1. Project Overview
CareFlow is a clinical pathway process-mining project. It analyses patient journeys to identify repeated activities, delays, and possible bottlenecks using synthetic hospital event data.

## 2. Dataset Details
- Unique patients: 500
- Event records: 3,351
- Dataset file: careflow_synthetic_500_patients.csv
- Data source: Synthetic data

Each row represents one hospital event for a patient.

## 3. Dataset Columns
- case_id: Patient or case identifier
- event_id: Unique event identifier
- event_order: Order of an event in the journey
- activity: Hospital activity
- timestamp: Date and time of the event
- department: Department handling the event
- journey_type: Type of patient journey
- is_loop_back: Indicates a marked loop-back
- data_source: Source of the data

## 4. Example Patient Journey
Registration → Triage → Doctor Consultation → Lab Test → Imaging → Treatment → Discharge

Actual journeys may differ between patients.

## 5. Loop-back Example
Registration → Triage → Doctor Consultation → Imaging → Triage → Doctor Consultation → Discharge

A repeated activity may indicate rework or a possible bottleneck. Further analysis is needed to identify the reason.

## 6. Project Workflow
Python → CSV Dataset → BigQuery → dbt → Process Mining → Power BI

Python generates the data, BigQuery stores it, dbt cleans and standardizes it, process mining analyses the journeys, and Power BI presents insights.

## 7. Initial Data Check
The initial check identified 500 unique patients, 3,351 event records, and no missing values. Duplicate events, timestamp order, and journey consistency still need further validation.

## 8. Important Note
This is synthetic data and does not represent real patients or actual hospital performance.
