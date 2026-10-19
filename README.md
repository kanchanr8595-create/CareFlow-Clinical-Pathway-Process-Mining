# CareFlow-Clinical-Pathway-Process-Mining
Clinical pathway process mining project using synthetic healthcare event logs to identify workflow bottlenecks, patient journey patterns, and process inefficiencies.

CareFlow is a healthcare process mining project that analyzes patient journey data to understand the flow of clinical activities across hospital departments. The project uses event log data to track each patient's pathway from registration and triage to doctor consultation, laboratory tests,treatment, and discharge.
The main objective is to identify the actual sequence of activities followed by patients, understand variations in patient journeys, detect repeated steps or loopbacks, and identify potential delays or inefficiencies in the clinical workflow. Python and data analysis techniques are used to clean, validate, and analyze the dataset, helping to generate insights that may support better workflow management and improved patient flow.
The dataset used in this project is synthetic, meaning it is generated for analysis and does not represent verified real-patient records.

# Column                     Meaning

Case_id                    Unique patient journey identifier
Event_id                   Unique identifier for each event
Event_order                Order in which an activity occurs
Activity                   Clinical activity,such as triage or Treatment
Timestamp                  Date and time of the activity
Department                 Hospital department handling the activity
Journey_type               Type of pathway:Noraml,Delayed,Loop-back or complex
Is_loop_back               Indicates whether an activity involves a return to an earlier step
Data_source                Indicates the origin of the data.

# Main Objective Of The Project

1. Data cleaning and validation:Check missing values,duplicate records,incorrect timestamps,and inconsistent event sequences.
2. Process flow analysis:Understands the order
