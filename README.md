CareFlow Clinical Pathway – Process Mining

Project Overview

CareFlow Clinical Pathway – Process Mining is a data analytics project focused on exploring healthcare event-log data to understand patient journeys and clinical workflows. The project uses event-level records to examine the sequence of activities, departments involved, and possible repeated steps in a patient's journey.

The project aims to prepare and validate structured healthcare event data for further analysis and process mining.

Project Objectives

- Set up a Google BigQuery environment for the CareFlow dataset.
- Load and explore the healthcare event-log data.
- Review the dataset schema and column data types.
- Validate record counts and check missing values in important fields.
- Organize SQL queries and document validation results.
- Prepare the data for further data-quality checks, dbt modelling, and process-mining analysis.

Tools and Technologies

- Google BigQuery – Cloud data storage, SQL queries, and data validation.
- SQL – Data exploration, schema inspection, record counting, and validation.
- dbt – Data transformation and modelling as part of the team workflow.
- Git and GitHub – Version control, project documentation, and team collaboration.

Dataset Details

- Google Cloud project: "care-flow-clinical-pathway"
- Dataset: "careflow_dataset"
- Source table: "care-flow-clinical-pathway-process-mining"
- Total records: 3,351
- Unique cases: 500
- Columns: 9

The dataset contains event-level information representing clinical pathway activities and their sequence.

Dataset Schema

Column| Data type| Description
"case_id"| STRING| Identifier for a patient journey or case
"event_id"| STRING| Identifier for an event
"event_order"| INT64| Sequence of an event within a case
"activity"| STRING| Clinical or workflow activity
"timestamp"| TIMESTAMP| Date and time associated with an event
"department"| STRING| Department associated with the event
"journey_type"| STRING| Classification of the clinical journey
"is_loop_back"| BOOL| Indicates whether an event represents a loop-back
"data_source"| STRING| Source associated with the event record

Work Completed: BigQuery Setup and Data Validation

My contribution to the project focuses on BigQuery setup, data loading, dataset exploration, and documentation.

- Set up and accessed the BigQuery project and dataset.
- Loaded the source CSV data into a BigQuery table.
- Reviewed the table schema and column data types.
- Executed SQL queries to verify the total record count.
- Retrieved sample records to inspect the loaded data.
- Checked missing values in key columns.
- Reviewed event ordering using "case_id" and "event_order".
- Documented the dataset schema, data workflow, validation checks, and privacy considerations.
- Organized SQL queries and validation results for team review.

Validation Results

Validation check| Result
Total records| 3,351
Unique cases| 500
Total columns| 9
Missing "case_id" values| 0
Missing "event_order" values| 0
Sample record inspection| First 10 records reviewed
Event ordering| Reviewed using "case_id" and "event_order"

These checks provide an initial validation of the data loaded into BigQuery. Additional data-quality checks, such as duplicate-event detection and timestamp consistency, are part of the broader project workflow.

Example SQL Queries

1. Count Total Records

SELECT COUNT(*) AS total_records
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`;

2. Preview Sample Records

SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
LIMIT 10;

3. Check Missing Values in Key Columns

SELECT
  COUNTIF(case_id IS NULL) AS missing_case_id,
  COUNTIF(event_order IS NULL) AS missing_event_order
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`;

4. Review Event Sequence

SELECT *
FROM `care-flow-clinical-pathway.careflow_dataset.care-flow-clinical-pathway-process-mining`
ORDER BY case_id ASC, event_order ASC;

Project Workflow

1. Data Setup: Create the BigQuery dataset and load the source event-log data.
2. Schema Exploration: Inspect column names, data types, and table structure.
3. Initial Validation: Check record counts, sample records, and missing values.
4. Data Quality: Perform further checks for duplicate events and timestamp consistency.
5. Data Transformation: Prepare staging models and transformations through the team's dbt workflow.
6. Process Mining: Use the prepared event log to investigate clinical pathways, activity sequences, and loop-back patterns.
7. Documentation and Collaboration: Maintain project notes, SQL queries, validation evidence, and updates in GitHub.

Data Privacy

Healthcare-related data should be handled according to the project's privacy requirements. Avoid publishing personally identifiable or confidential patient information in the repository, screenshots, or documentation.

Current Contribution

Role: BigQuery Setup and Data Loading

My responsibilities include BigQuery dataset and table setup, loading the source data, inspecting the schema, running initial validation queries, and documenting the results for team collaboration.

The broader project includes data-quality validation, dbt modelling, and process-mining analysis by the team.

Conclusion

The BigQuery setup and initial validation work establishes a foundation for the CareFlow Clinical Pathway project. The documented schema, SQL queries, and validation results support subsequent data-quality checks, transformation workflows, and clinical pathway analysis.
