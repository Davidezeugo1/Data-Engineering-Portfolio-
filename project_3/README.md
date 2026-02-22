# Project 3- Credit Card transaction pipeline
## Overview

This project documents a successful end-to-end batch OTLP pipeline.

The pipeline demonstrates how data is:

Orchestrated with Apache Airflow

Processed using Apache Spark (batch mode)

Persisted into MongoDB 

Tranisfromed in spark 

strong in MySQL for analytical dashboards.  

This project serves as the foundation for later streaming pipelines and proves the cluster is production-capable

## Pipeline Structure

* Airflow DAG:
  * Trigger batch job
  * Performs validation checks
  * Submits Spark jobs using spark-submit

* Spark Batch Job
  * Reads source data
  * Applies schema enforcement
  * Writes final documents to MongoDB

* MongoDB Sink
  * Stores transformed documents
  * Indexed for query efficiency
  * Used later as a streaming source

## ✅ Key Leason:
  
* Learned to use the correct connector
* Learned to version control
* Learned to create the coonection for airflow to spark
* Learned to debug spark error


## ✅ Key Achievements:
* Fully working multi-node Spark cluster

* Airflow successfully triggering Spark jobs

* Reliable data ingestion into MongoDB

## DAG:
* spark_to_mongo can be found active on the airflow UI ** http://192.168.0.100:8085/home/  



Project details coming soon.
