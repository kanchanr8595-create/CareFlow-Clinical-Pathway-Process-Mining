# CareFlow-Clinical-pathway-Process

In this dataset has a timestamp column containing date and time values, such as 2026-09-11 09:54:00.

## Timestamp Validation: Converted the timestamp column from text to Pandas datetime format. No invalid timestamps were identified. The timestamps were also checked for chronological consistency within each patient's journey, and no backward timestamp sequences were detected.

checks and validation done here are:


  # VALIDATION                                       RESULT
## a.Timestamp Conversion--                          Successful
## b.Invalid timestamps--                               0
## c.Earliest timestamps--                           1 september 2026,09:16
## d.Latest timestamp--                              15 september 2026,04:11
## e.Final data type--                               datetime64[ns]


# In our project,timestamps helps us:

## 1.Understand the order in which clinical activities occur.
## 2.calculate the time between registration, triage, consultaion and other activities.
## 3.Identify the delays in a patient's clinical pathway.
## 4.Study repeated activities and loop-back.
## 5.Analyse the duration of patient's journey.
