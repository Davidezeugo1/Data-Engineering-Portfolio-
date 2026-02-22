# Project 3- Credit Card transaction pipeline
## Overview

This project documents a successful end-to-end batch OTLP pipeline.

The pipeline demonstrates how data is:

Orchestrated with Apache Airflow

Processed and transformed using Apache Spark

Persisted into MongoDB and MYSQL 

visualized in dashborad.


## Pipeline Structure

* Airflow DAG:
  * Trigger job to generate data and persist data into the database (MongoDB)
  * Submits Spark jobs using spark-submit to handle transformations

* Spark Batch Job
  * Reads source data
  * Applies schema enforcement
  * Writes final documents to MYSQL

* MongoDB Sink
  * Stores raw data
    
* MySQL
  * Stores transformed data
  * accessible by a BI tool for analytical processes. 


## ✅ Key Achievements:
* Fully working OTPL pipeline

* Airflow successfully triggering Python and Spark jobs

* Reliable data ingestion into MongoDB and MYSQL

* Accessible with BI tools to create dashboards 

## DAG:
* (Name for dag here) can be found active on the airflow UI ** http://192.168.0.100:8085/home/  
