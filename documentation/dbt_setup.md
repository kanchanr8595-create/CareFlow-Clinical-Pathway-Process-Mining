
# CareFlow dbt Setup

## Project Overview

CareFlow is a clinical pathway process-mining project. The goal is to prepare hospital event data for process analysis.

## What Is dbt?

dbt (data build tool) helps data engineers transform data using SQL models and validate the results with tests.

## Role of dbt in CareFlow

The team plan uses BigQuery to store raw hospital event data. dbt will transform the raw data into a consistent format for downstream validation and process mining.

## My Responsibilities

- Document dbt setup.
- Define the raw data source.
- Build the first staging model.
- Add suitable data-quality tests.
- Document execution results and blockers.

## Current Status

Documentation started. BigQuery access and the existing raw table details must be confirmed before running the models.

## CareFlow Data Workflow

1. Generate sample hospital events using Python.
2. Store the raw event data in BigQuery.
3. Use dbt to standardize and clean the event data.
4. Validate the transformed data.
5. Prepare the cleaned event log for process mining.

The actual model execution depends on BigQuery access and the availability of the raw event table.

## Raw Event Source Definition

The dbt source should point to the raw hospital event table stored in BigQuery.

Before creating the final source configuration, confirm:

- BigQuery project ID
- Dataset name
- Raw table name
- Actual column names and data types

Expected event fields may include a case identifier, activity name, and event timestamp. These must be checked against the team's actual dataset before implementation.

The source definition will be maintained in the dbt project's YAML configuration.


